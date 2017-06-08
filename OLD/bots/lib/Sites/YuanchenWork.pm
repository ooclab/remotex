package Sites::YuanchenWork;
use utf8;
use Mojo::Base 'Sites';
use Agent;
use Common qw/clean_text str2date Dumper is_utf8 encode decode/;
use Time::Piece;

has max_page_number   => 1;
has uniq_prefix       => 'yuanchen_work';
has start_page_number => 1;
has ua                => sub { Agent->new };
has url               => 'http://yuancheng.work/page/1';

sub go {
    my $self      = shift;
    my $start_url = shift || $self->url;
    my $max_page  = shift || $self->max_page_number;

    my @items;
    while ( $start_url && $max_page ) {
        $max_page--;

        my $tx = $self->ua->get($start_url);

        return \@items unless $tx->success;
        my $dom = $tx->res->dom;

        $dom->find('li[class="list-group-item "]')->each(
            sub {
                my $e    = shift;
                my $item = {};
                $item->{platform} = '远程';
                $item->{title}    = clean_text( $e->find('h4')->first->text );
                $item->{url}      = $e->find('a[class="list-group-item-body"]')->first->attr('href');
                $e->find('a[class^="label"]')->each(
                    sub {
                        my $e = shift;
                        push @{ $item->{tags} }, clean_text( $e->all_text );
                    }
                );

                $item->{date_str}     = $e->find('span[class="date"]')->first->text;
                $item->{release_date} = parse_date( str2date( $item->{date_str} ) );
                ( $item->{checksum} ) = $item->{url} =~ /(\d+)\.html/;
                $item->{checksum} = sprintf '%s_%s', $self->uniq_prefix, $item->{checksum};

                $item = $self->parse_content($item);

                $self->output($item);
                push @items, $item;
            }
        );

        $start_url = $self->parse_next_url($dom);
    }

    return \@items;
}

sub parse_date {
    my $str = shift;
    return unless $str;
    my $t = Time::Piece->strptime( $str, "%Y-%m-%d" );
    my $t_s =$t->strftime("%Y-%m-%dT%H:%M:%S.%sZ");

    $t_s =~ s/\d\d\d\dZ$/Z/;
    return $t_s;
}

sub parse_content {
    my $self = shift;
    my $item = shift;

    return $item unless $item->{url};

    my $content_dom = $self->ua->get_cache_url( $item->{url} );

    $item->{content} = clean_text( $content_dom->find('div[class="job-detail"]')->first->all_text );

    #$item->{content} = decode( 'utf8', $item->{content} ) if is_utf8( $item->{content } );

    return $item;
}

sub parse_next_url {
    my $self = shift;
    my $dom  = shift;

    my $url = $dom->find('li[class="next-page"] > a')->first;
    return unless $url;
    return $url->attr('href');
}
1;

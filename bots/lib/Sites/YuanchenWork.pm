package Sites::YuanchenWork;

use Mojo::Base -base;
use Agent;
use Common qw/clean_text str2date Dumper/;

has max_page_number   => 99;
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
                $item->{title} = clean_text( $e->find('h4')->first->text );
                $item->{url}   = $e->find('a[class="list-group-item-body"]')->first->attr('href');
                $e->find('a[class^="label"]')->each(
                    sub {
                        my $e = shift;
                        push @{ $item->{tags} }, clean_text( $e->all_text );
                    }
                );

                $item->{date_str} = $e->find('span[class="date"]')->first->text;
                $item->{date}     = str2date( $item->{date_str} );
                ( $item->{uniq_id} ) = $item->{url} =~ /(\d+)\.html/;
                $item->{uniq_id} = sprintf '%s_%s', $self->uniq_prefix, $item->{uniq_id};

                $self->parse_content($item);
                print Dumper($item);
                push @items, $item;
            }
        );

        $start_url = $self->parse_next_url($dom);
    }

    return \@items;
}

sub parse_content {
    my $self = shift;
    my $item = shift;

    return $item unless $item->{url};

    my $content_dom = $self->ua->get_cache_url( $item->{url} );

    $item->{content} = clean_text( $content_dom->find('div[class="job-detail"]')->first->all_text );
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

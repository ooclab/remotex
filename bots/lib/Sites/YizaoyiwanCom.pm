package Sites::YizaoyiwanCom;
use utf8;
use Mojo::Base 'Sites';
use Agent;
use Common qw/clean_text str2date Dumper is_utf8 encode decode/;
use Time::Piece;

has max_page_number   => 99;
has uniq_prefix       => 'yizaoyiwan_com';
has start_page_number => 1;
has ua                => sub { Agent->new };
has url               => 'http://yizaoyiwan.com/categories/employer';

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

        $dom->find('li[class="discussion list-group-item"]')->each(
            sub {
                my $e    = shift;
                my $item = {};
                $item->{platform} = '一早一晚';

                my $title = $e->find('div[class="media-heading"] > a')->first;
                if ($title) {
                    $item->{title} = clean_text( $title->text );
                    $item->{url}   = $title->attr('href');
                    if ( $item->{url} ) {
                        my $url = Mojo::URL->new( $item->{url} );
                        unless ( $url->is_abs ) {
                            $item->{url} = $url->to_abs( Mojo::URL->new( $self->url ) )->to_string;
                        }
                    }
                }

                $item->{release_date} = parse_date( $e->find('time[class="timeago"]')->first->attr('datetime') );

                $item->{date_str} = $item->{release_date};

                ( $item->{checksum} ) = $item->{url} =~ /(\d+)$/;
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
    my $t = Time::Piece->strptime( $str, "%Y-%m-%d %H:%M:%S" );
    return $t->strftime("%Y-%m-%dT%H:%M:%SZ");
}

sub parse_content {
    my $self = shift;
    my $item = shift;

    return $item unless $item->{url};

    my $content_dom = $self->ua->get_cache_url( $item->{url} );

    $item->{body}       = clean_text( $content_dom->find('div[class="post-content"]')->first->all_text );
    $item->{view_count} = clean_text( $content_dom->find('div[class="media-meta text-muted"]')->first->all_text );

    ( $item->{view_count} ) = $item->{view_count} =~ /(\d+)\s*次阅读/;

    return $item;
}

sub parse_next_url {
    my $self = shift;
    my $dom  = shift;

    my $url = $dom->find('a[rel="next"]')->first;
    return unless $url;
    return $url->attr('href');
}
1;

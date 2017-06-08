package Sites::SegmentfaultCom;
use utf8;
use Mojo::Base 'Sites';
use Agent;
use Common qw/clean_text Dumper to_json/;
use Time::Piece;

has max_page_number   => 1;
has uniq_prefix       => 'segmentfault_com';
has start_page_number => 1;
has ua                => sub { Agent->new };
has url               => 'https://segmentfault.com/jobs/search?page=';

sub go {
    my $self      = shift;
    my $start_url = shift;
    my $max_page  = shift || $self->max_page_number;

    my $current_page = 1;
    $start_url = $self->build_url($current_page);

    my @items;

    while ( $start_url && $max_page && $current_page <= $max_page ) {
        $max_page--;
        $current_page++;

        my $headers = {
            'Pragma'                    => 'no-cache',
            'Accept-Encoding'           => 'gzip, deflate, sdch, br',
            'Accept-Language'           => 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
            'Upgrade-Insecure-Requests' => '1',
            'User-Agent'                => 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Accept'                    => 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer'                   => 'https://segmentfault.com/jobs/search',
            'Connection'                => 'keep-alive',
            'Cache-Control'             => 'no-cache',
        };
        my $tx = $self->ua->get( $start_url => $headers );

        my $dom = $tx->res->dom;
        unless ($dom) {
            undef $current_page;
            last;
        }

        foreach my $e ( $dom->find('section[class="stream-list__item row"]')->each ) {
            my $item = {};
            $item->{platform} = 'segmentfault';

            $item->{title} = $e->find('a[class="job-name"]')->first;
            if ( $item->{title} ) {
                $item->{url} = sprintf "https://segmentfault.com%s", $item->{title}->attr('href');
                $item->{title} = $item->{title}->all_text;
            }

            my ($id) = $item->{url} =~ /\/(\d+)$/;
            $item->{checksum} = $self->build_checksum($id);

            my $price = $e->find('strong[class="text-green"]')->first->all_text;
            $price = clean_text($price);
            if ($price) {
                my ($low_price) = $price =~ /(\d+)/;
                $item->{price} = $low_price * 1000 if $price =~ /k/i && $low_price;
            }

            my $date = $e->find('span[class="pull-right text-muted mt10"]')->first->all_text;
            if ($date) {
                my $now = DateTime->now( time_zone => 'Asia/Shanghai' );

                if ( $date =~ /前/ ) {
                    my ($num) = $date =~ /(\d+)/;
                    if ($num) {
                        $date = $now->subtract( hours  => $num )->strftime('%Y年%m月%d日 %H:%M:%S') if $date =~ /小时/;
                        $date = $now->subtract( days   => $num )->strftime('%Y年%m月%d日 %H:%M:%S') if $date =~ /天/;
                        $date = $now->subtract( months => $num )->strftime('%Y年%m月%d日 %H:%M:%S') if $date =~ /月/;
                    }
                }
                $date = sprintf '%s年%s', DateTime->now( time_zone => 'Asia/Shanghai' )->year, $date unless $date =~ /年/;
                $date =~ s/月|年/-/g;
                $date =~ s/日//;

                my $t = Time::Piece->strptime( $date, "%Y-%m-%d %H:%M:%S" );
                $item->{release_date} = $t->strftime("%Y-%m-%dT%H:%M:%S.%sZ");
                $item->{release_date} =~ s/\d\d\d\dZ$/Z/;
            }

            $item->{city} = $e->find('span[class="text-muted"]')->first->all_text;
            $item->{city} =~ s/\[\]//g if $item->{city};

            $e->find('li[class="tagPopup"] a')->each(
                sub {
                    my $skill = shift;
                    push @{ $item->{skills} }, $skill->all_text;
                }
            );

            $e->find('p[class="text-muted"]')->each(
                sub {
                    my $c = shift;
                    return unless $c;
                    map { push @{ $item->{categories} }, $_ unless /^\s*$/ } (split /\\|\/|·|\s+/, $c->all_text );
                }
            );

            $item = $self->parse_content($item);

            $self->output($item);
            push @items, $item;
        }

        $start_url = $self->build_url($current_page);
    }

    return \@items;
}

sub parse_content {
    my $self = shift;
    my $item = shift;

    return $item unless $item->{url};

    my $content_dom = $self->ua->get_cache_url( $item->{url} );

    $content_dom->find('div[class="fmt"]')->each(
        sub {
            my $e = shift;
            $item->{body} .= $e->all_text;
        }
    );

    my $tmp = $content_dom->find('span[class="job-detail__func-desc"] strong')->to_array;
    shift @$tmp;
    my $view_count = shift @$tmp;
    if ($view_count) {
        $item->{view_count} = $view_count->all_text;
    }
    $item->{body} = clean_text( $item->{body} );

    return $item;
}

sub build_url {
    my $self = shift;
    my $page = shift;
    return unless $page;
    return sprintf "%s%s", $self->url, $page;
}

1;

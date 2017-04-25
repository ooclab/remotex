package Sites::CodingNet;
use utf8;
use Mojo::Base 'Sites';
use Agent;
use Common qw/clean_text Dumper/;

has max_page_number   => 99;
has uniq_prefix       => 'coding_net';
has start_page_number => 1;
has ua                => sub { Agent->new };
has url               => 'https://mart.coding.net/api/reward/list?type=&status=&role_type_id=&page=1';

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

        my $tx = $self->ua->get($start_url);

        return \@items unless $tx->success;
        my $dom = $tx->res->json;
        last unless $dom;

        undef $current_page if $dom->{data}->{page} >= $dom->{data}->{totalPage};

        foreach my $e ( @{ $dom->{data}->{list} } ) {

            my $item = {};

            $item->{title} = $e->{title};
            $item->{url} = sprintf "https://mart.coding.net/project/%s", $e->{id};

            $item->{checksum} = $self->build_checksum( $e->{id} );
            $item->{price}    = $e->{formatPriceNoCurrency};
            $item->{price} =~ s/,//g if $item->{price};

            $item->{release_date}     = $e->{roleTypes}->[0] ? $e->{roleTypes}->[0]->{created_at} : undef;
            
            $item->{view_count} = $e->{applyCount};

            if ( $e->{roleTypes} ) {
                map { push @{$item->{role}}, $_->{name} || $_->{description} } @{$e->{roleTypes}};
            }
            push @{ $item->{categories} }, 'Web网站' if $e->{type} == 0;
            push @{ $item->{categories} }, '其它'    if $e->{type} == 4;

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

    $content_dom->find('div[class="content-group"]')->each(
        sub {
            my $e = shift;
            $item->{body} .= $e->all_text;
        }
    );

    $item->{body} = clean_text( $item->{body} );
    $item->{status} = clean_text( $content_dom->find( 'span[class^="status"]')->first->all_text );

    return $item;
}

sub build_url {
    my $self = shift;
    my $page = shift;
    return unless $page;
    return sprintf "https://mart.coding.net/api/reward/list?type=&status=&role_type_id=&page=%s", $page;
}
1;

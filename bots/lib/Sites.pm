package Sites;

use Mojo::Base -base;
use Common qw/to_json/;

sub output {
    my $self = shift;
    my $item = shift || {};

    say to_json( $item );
}

sub build_uniq_id {
    my $self = shift;
    my $id = shift;
    return sprintf '%s_%s', $self->uniq_prefix, $id;
}

1;

package Sites;

use Mojo::Base -base;
use Common qw/to_json/;

sub output {
    my $self = shift;
    my $item = shift || {};


    say to_json( $item );
}

1;

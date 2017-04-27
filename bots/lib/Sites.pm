package Sites;

use Mojo::Base -base;
use Common qw/to_json Dumper/;
use Agent;

has url_base => 'https://remotex.ooclab.org';
has ua => sub { Agent->new };

sub output {
    my $self    = shift;
    my $item    = shift || {};
    my $api_url = '/api/spider/jobx/job';

    my $url = Mojo::URL->new($api_url)->base( Mojo::URL->new( $self->url_base ) )->to_abs;

    my $headers = {
        'Content-Type' => 'application/json',
        Authorization  => 'Basic dXNlcjE6NDVhYTczNmYxZjY2ZTUxMWEyOWIwYzJi',
    };

    #die Dumper $item;
    my $json = $self->ua->post( $url => $headers => json => $item )->res->dom;

    if ( $json->{errmsg} ) {
        say "Fail:  " . $json->{errmsg} . to_json( $item );
    }
}

sub build_checksum {
    my $self = shift;
    my $id   = shift;
    return sprintf '%s_%s', $self->uniq_prefix, $id;
}

1;

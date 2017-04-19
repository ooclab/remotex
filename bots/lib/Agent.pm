package Agent;

use Common qw/url2file slurp_file url2path/;
use Mojo::Base 'Mojo::UserAgent';

use constant DEBUG => $ENV{REMOTEX_DEBUG} || 0;

sub new {
    my $class = shift;
    my $self  = $class->SUPER::new(@_);
    
    return $self;
}


sub get_cache_url {
    my $self = shift;
    my $url = shift;

    return unless $url;
    my $file = url2file( $url );
    return Mojo::DOM->new( slurp_file( $file ) ) if -e $file;
    my $file_path = url2path( $url );
    `mkdir -p $file_path`;
     
    my $tx = $self->get( $url );
    return unless $tx->success;
    
    open my $fh, '>', $file || die "Can't open file: $!\n";
    print $fh $tx->res->body;
    close $fh;
    return $tx->res->dom;
}

1;

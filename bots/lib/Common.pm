package Common;
use Mojo::Base -strict;

use Carp qw/carp croak/;
use Data::Dumper qw/Dumper/;
use Digest::MD5 qw/md5_hex/;

use Encode qw/find_encoding encode decode is_utf8/;
use Exporter 'import';
use Time::HiRes ();
use DateTime;
use YAML::Syck qw/LoadFile/;
use Path::Tiny qw/path/;

use Mojo::File;


use JSON qw/to_json from_json/;

use constant MONOTONIC => eval { !!Time::HiRes::clock_gettime( Time::HiRes::CLOCK_MONOTONIC() ) };

our @EXPORT_OK = ( qw/crap croak/, qw/Dumper/, qw/md5_hex/, qw/find_encoding encode decode is_utf8/, qw/url_escape url_unescape/, qw/to_json from_json/, qw/slurp_file url2file url2path clean_text/, qw/str2date/, qw/config/ );

#our @EXPORT = @EXPORT_OK;

sub url_escape {
    my ( $str, $pattern ) = @_;
    if   ($pattern) { $str =~ s/([$pattern])/sprintf '%%%02X', ord $1/ge }
    else            { $str =~ s/([^A-Za-z0-9\-._~])/sprintf '%%%02X', ord $1/ge }
    return $str;
}

sub url_unescape {
    my $str = shift;
    $str =~ s/%([0-9a-fA-F]{2})/chr hex $1/ge;
    return $str;
}

sub clean_text {
    my $str = shift;
    return unless $str;
    $str =~ s/^\s*//g;
    $str =~ s/\s+//g;
    $str =~ s/\s*$//g;
    return $str;
}

sub str2date {
    my $date = shift;
    return unless $date;
    my ( $day ) = $date =~ /(\d+)/;
    return unless $day;

    $day *= 30 if $day =~ /月前/;
    $day *= 30 * 12  if $day =~ /年前/;

    return now()->subtract( days => $day )->strftime( '%Y-%m-%d' );
}

sub now {
    return DateTime->now( time_zone => 'Asia/Shanghai' );
}


sub url2path {
    my $url = shift;
    return unless $url;

    my $url_md5 = md5_hex( $url );
    
    my $dir = join( '/', (map { substr $url_md5, 0, $_ } qw/2 4 6 8/ ) );
    my $cache_path = config()->{cache_path} || 'caches';
    return sprintf '%s/%s/%s/%s', root(), $cache_path, $dir, $url_md5;
}

sub url2file {
    my $url = shift;
    my $path = url2path( $url );
    return unless $path;
    return sprintf '%s/orig.html', $path;
}

sub slurp_file {
    my $file = shift;
    return unless -e $file;

    my $mf = Mojo::File->new( $file ); #, '<:encoding(UTF-8)' );
    return $mf ->slurp;
}

sub config {
   state $config;
   return $config if $config;
    
   my $conf = sprintf '%s/%s/%s', root(), 'conf', 'main.yaml';
   return {} unless -e $conf;
   $config = LoadFile( $conf );
   return $config;
}

sub root {
    state $root_path = path(__FILE__)->absolute->parent->parent;
    return path( $root_path, @_ );
}

1;

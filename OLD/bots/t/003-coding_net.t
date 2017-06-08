#!/usr/bin/env perl

use Mojo::Base -strict;
use FindBin qw/$Bin/;
use lib "$Bin/../lib";

use Test::More;
use Sites::CodingNet;

my $yw = Sites::CodingNet->new;
$yw->go;

done_testing();

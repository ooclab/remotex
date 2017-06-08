#!/usr/bin/env perl

use Mojo::Base -strict;
use FindBin qw/$Bin/;
use lib "$Bin/../lib";

use Test::More;
use Sites::YuanchenWork;

my $yw = Sites::YuanchenWork->new;
$yw->go;

done_testing();

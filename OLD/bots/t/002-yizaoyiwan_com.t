#!/usr/bin/env perl

use Mojo::Base -strict;
use FindBin qw/$Bin/;
use lib "$Bin/../lib";

use Test::More;
use Sites::YizaoyiwanCom;

my $yw = Sites::YizaoyiwanCom->new;
$yw->go;

done_testing();

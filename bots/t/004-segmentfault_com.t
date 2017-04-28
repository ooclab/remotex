#!/usr/bin/env perl

use Mojo::Base -strict;
use FindBin qw/$Bin/;
use lib "$Bin/../lib";

use Test::More;
use Sites::SegmentfaultCom;

my $bot  = Sites::SegmentfaultCom->new;
$bot->go;

done_testing();

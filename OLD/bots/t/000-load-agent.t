#!/usr/bin/env perl

use Mojo::Base -strict;
use FindBin qw/$Bin/;
use lib "$Bin/../lib";

use Test::More;

require_ok( 'Agent' );
require_ok( 'Sites::YuanchenWork');
require_ok( 'Sites::YizaoyiwanCom');

done_testing();

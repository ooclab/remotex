## 概述
remotex 项目数据爬虫,  使用perl( 5.24.0 ).

安装依赖模块推荐使用:

- cpanm( https://github.com/miyagawa/cpanminus ) 
- cpm ( https://github.com/skaji/cpm ) 

进行安装.  安装方法: 

	cpanm Mojo::UserAgent
	


## 依赖模块
- [Perl 5.24.0 ](http://perl.org)
- [Mojo::UserAgent](https://metacpan.org/pod/Mojo::UserAgent)
- [Mojo::File](https://metacpan.org/pod/Mojo::File)
- [Digest::MD5](https://metacpan.org/pod/Digest::MD5)
- [Encode](https://metacpan.org/pod/Encode)
- [Time::HiRes](https://metacpan.org/pod/Time::HiRes)
- [DateTime](https://metacpan.org/pod/DateTime)
- [YAML::Syck](https://metacpan.org/pod/YAML::Syck)
- [Path::Tiny](https://metacpan.org/pod/Path::Tiny)
- [JSON](https://metacpan.org/pod/JSON)

## 执行方法
默认, 每个网站写一个 test 存放在 t 目录下, 

    cd remotex
    perl t/001-yuancheng_work.t

相关方法可以放到 crontab 里


## TOTO
- 建立数据库表
- 返回数据存数据库



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


## TODO
- 建立数据库表
- 返回数据存数据库

## Bots List
- [ √ ] [远程.work](http://yuancheng.work/)
- [ √ ] [一早一晚](http://yizaoyiwan.com/categories/employer)
- [ x ] [SegmentFault 招聘](http://yizaoyiwan.com/categories/employer)( 无数据 )
- [ √ ] [码市](https://mart.coding.net/)
- [  ] [实现网]
- [  ] [V2EX]
- [  ] [V2MM]
- [  ] [大鲲](https://pro.lagou.com/)
- [  ] [英选](https://www.linktion.cn/)
- [  ] [程序员客栈](https://www.proginn.com/)
- [  ] [厘米脚印](http://www.limijiaoyin.com/)
- [  ] [实现网](http://shixian.com/)
- [  ] [小圆桌](http://xiaoyuanzhuo.com/)
- [  ] [自由人](http://www.freemancn.com/)
- [  ] [有轻功](http://www.youqinggong.com/)
- [  ] [云沃客](https://www.clouderwork.com/)



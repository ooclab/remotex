## 概述
docker 目录下的文件用于构建 spider-perl Docker 容器(不确定概念是否正确, 请指正.  :-) ). 用于布署 remotex perl 编写的 spider.


## 文件说明

1. docker-build.sh 用于构建 docker 容器, 使用方法

	./docker-build.sh
	
2. Dockerfile: docker 的定义文件
3. docker-compose.yaml Docker compose 定义文件.


## 布署步骤

环境需求: 

	1. perl, 建议大于 perl 5.10
	2. docker
	3. docker-compose

构建步骤:

	1. git clone https://github.com/ooclab/remotex
	2. cd remotex/bots/docker/
	3. ./docker-build.sh
	4. docker-compose up -d
	5. docker-compose exec spider-perl bash (用于登入 docker, 查看相关运行情况, 非必须步骤. 退出 docker 直接输入 exit 即可)
	6. docker run -it --rm remotex/spider-perl (手动运行一次spider )
	7. 可根据情况建立 crontab, 建议每10分钟运行1次.

	
## 感谢
感谢 @gwind 耐心的演示. 使我对 Docerk 有了全新的认识!

有任何问题, 欢迎发 pr 给我. 谢谢.
	

# Scrapy spider开发说明

Remotex 使用scrapy spider爬取信息。scrapy（https://scrapy.org ）一个基于Python的高效爬虫框架。

## 目录结构及注意文件说明

```
PyBots/
    scrapy.cfg            # 配置文件
    PyBots/               # 项目代码目录
        __init__.py
        items.py          # 爬取内容数据结构定义
        pipelines.py      # 数据爬取后处理程序，负责调用存储API
        settings.py       # 项目设置文件
        spiders/          # 爬虫文件目录，每个网站提供一个文件
            __init__.py
```

## 开发指南

Spider 主要方法说明，示例spider如下

```python
import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"#名称，运行spider也使用这个名称
    allowed_domains = ["abc.com"]#允许爬取域名
    start_urls = [
        "http://abc.com/"#起始url
    ]

    def parse(self, response):#运行spider的主方法
        # 回调处理子页面示例
        for href in response.css('.author + a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_author)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
```

## 手动运行spider方法

```
scrapy crawl 爬虫名称
```

## 运行部署

- 生产环境使用scrapyd运行spider，方便管理。可以配置权限和检查spider运行日志
- 使用scrapyd-client发布spider，每次发布自动生成版本，方便管理和调度
  参考http://blog.wiseturtles.com/posts/scrapyd.html
- 由于scrapyd极其不稳定，需要使用supervisord值守程序保障scrapyd的运行

## Docker

### 准备环境

#### 安装 docker

使用 CentOS , Ubuntu 等最新版 Linux 系统，运行：

```
curl -fsSl https://get.docker.com | sh
```

或者

```
curl -fsSl https://test.docker.com | sh
```

安装最新版 docker

#### 安装 docker-compose

下载并 copy 到 /usr/local/bin

### 运行测试示例

首次运行，需要编译 `remotex/scrapy` docker image :

```
$ ./docker-build.sh
```

启动 scrapy 容器：

```
$ docker-compose up -d
```

进入 scrapy 容器：

```
$ docker-compose exec scrapy bash
```

运行 spider :

```
# scrapy crawl lagou
```

关闭，并清理容器：

```
$ docker-compose down
```

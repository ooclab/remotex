# remotex api

我们使用 kong 作为 API 前端 api gateway 角色.使用微服务架构开发各个具体 api 模块.

目前使用 `remotex api` 的角色:

- 前端(Web) : 暂时不需要认证,可以直接调用 Jobx 微服务的接口展示信息
- 爬虫 : 需要认证,向数据库添加数据

## 认证

目前使用 [Basic Authentication](https://getkong.org/plugins/basic-authentication/) , _暂时只有爬虫上传数据需要调用_ .

## 模块(微服务)

### Jobx(信息发布)

聚合各大平台/论坛的远程/兼职/外包/众包等职位信息.

#### 技术堆栈

- Python3
- Tornado
- SQLAlchemy

参考: https://github.com/ooclab/eva

## 数据分析

### kibana

```
docker run --name some-kibana --link api_es_1:elasticsearch --network api_default -p 5601:5601 -d kibana:5.3.0
```

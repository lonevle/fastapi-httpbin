# fastapi-httpbin

这是一个使用fastapi构建的简易httpbin服务,用于接口测试。



## 特性

- 主要特性: 不受路径参数限制, 根据不同请求类型自动处理get和post请求
- 支持GET和POST请求
- 自动返回请求信息
    - query参数
    - form表单数据
    - json数据
    - 请求header
    - 文件数据(base64编码)
- 添加CORS支持

>不受路径参数限制, 所以可以用于测试nginx等代理的转发

## 用法

```
python httpbin.py
```

然后可以发送GET或POST请求访问:

```
curl http://localhost:8010/get?foo=bar
```

它将返回如下信息:

```json
{
  "args": {
    "foo": "bar"    
  },
  "headers": {
    "Accept": "*/*",
    "Host": "localhost:8010",
    "User-Agent": "curl/7.64.1"
  },
  "origin": "127.0.0.1",
  "url": "http://localhost:8010/get?foo=bar"
}
```

> 也可以使用 curl http://localhost:8010/post?foo=bar 处理方式与路径参数无关, 只与请求类型有关

对于POST请求,它将返回表单数据、JSON和文件:

```
curl -X POST http://localhost:8010/post -d 'foo=bar' -H 'Content-Type: application/json' -d '{"hello": "world"}' --data-binary '@file.txt' 
```

```json
{
  "args": {},
  "data": "", 
  "files": {
    "file": "dGVzdCBmaWxlIGNvbnRlbnQ="
  },
  "form": {
    "foo": "bar"
  },
  "headers": {
    "Content-Type": "application/json",
    "Host": "localhost:8010",
    "Content-Length": "33"
  },
  "json": {
    "hello": "world"
  },
  "origin": "127.0.0.1",
  "url": "http://localhost:8010/post"
}
```

## TODO

- 支持更多请求类型
- 返回更多请求信息
- 添加测试用例

欢迎贡献和提交问题!
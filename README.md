# fastapi-httpbin

This is a simple httpbin service built with fastapi for API testing. 

[🇨🇳 中文](README.zh-CN.md)

## Features

- Main feature: Handle GET and POST requests automatically regardless of path parameter

- Support GET and POST requests  

- Auto return request info

  - Query params
  - Form data
  - JSON body
  - Request headers
  - File data (base64 encoded)

- Add CORS support

> Handle requests regardless of path, useful for testing proxy/nginx redirect

## Usage

```
python httpbin.py
```

Then you can send GET or POST requests to: 

```
curl http://localhost:8010/get?foo=bar
```

It will return info like:

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

> You can also use curl http://localhost:8010/post?foo=bar, path doesn't matter, only request type.

For POST requests, it will return form data, JSON and files:

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

- Support more request types
- Return more request info 
- Add test cases

Feel free to contribute and open issues!
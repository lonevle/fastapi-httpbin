from typing import Union

from fastapi import FastAPI, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.datastructures import UploadFile
import base64
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{path:path}")
async def get(request: Request):
    client_host = request.client.host
    forwarded_for = request.headers.get('X-Forwarded-For')

    real_ip = forwarded_for.split(',')[0] if forwarded_for else client_host
    return {
        "args": request.query_params,
        "headers": request.headers,
        "origin": real_ip,
        "url": request.url._url
    }

@app.post("/{path:path}")
async def post(request: Request):
    client_host = request.client.host
    forwarded_for = request.headers.get('X-Forwarded-For')

    real_ip = forwarded_for.split(',')[0] if forwarded_for else client_host
    try:
        files = {}
        form_data = {}
        form = await request.form()
        for key, value in form.items():
            if isinstance(value, UploadFile):
                content = await value.read()
                file_content = base64.b64encode(content).decode('utf-8')
                files[key] = file_content
            else:
                form_data[key] = value

    except Exception as e:
        form_data = {
            "error":"form %s" % e
        }
    try:
        json = await request.json()
    except:
        json = {}
    try:
        body = await request.body()
    except Exception as e:
        body = b""

    return {
        "args": request.query_params,
        "data": body.decode("utf-8"),
        "files": files,
        "form": form_data,
        "json": json,
        "headers": request.headers,
        "origin": real_ip,
        "url": request.url._url
    }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8010)
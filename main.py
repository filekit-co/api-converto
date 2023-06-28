
import os

import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from api import pdf_kit, to_doc, to_docx, to_pdf

app = FastAPI(title='Converto pdf api server')


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routers = [
    to_doc.router,
    to_docx.router,
    to_pdf.router,
    pdf_kit.router,
]

for router in routers:
    app.include_router(router)


@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    # after process
    response = await call_next(request)
    # 기존 응답 헤더에 'Access-Control-Expose-Headers' 헤더를 추가합니다.
    # CORS 정책으로 인해 Content-Disposition를 sveltekit이 못가져올 경우가 존재합니다.
    # Content-Disposition는 파일 이름을 전달하기 위해 필요합니다.
    response.headers["Access-Control-Expose-Headers"] = "Content-Disposition"
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get('PORT', 8001)), log_level="info")

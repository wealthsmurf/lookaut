import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/Bgggm.mp3")
async def get_audio():
    return FileResponse('Bgggm.mp3')

if __name__ == "__main__":
    # Railway가 제공하는 포트를 읽어옴, 기본값은 8080
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

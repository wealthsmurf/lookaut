import os
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

# 현재 main.py 파일이 있는 디렉토리 경로를 가져옵니다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
async def read_index():
    html_path = os.path.join(BASE_DIR, "templates/index.html")
    # 파일이 존재하는지 확인 후 전송 (에러 방지)
    if os.path.exists(html_path):
        return FileResponse(html_path)
    return HTMLResponse(content="<h1>index.html 파일을 찾을 수 없습니다.</h1>", status_code=404)

@app.get("/Bgggm.mp3")
async def get_audio():
    audio_path = os.path.join(BASE_DIR, "Bgggm.mp3")
    if os.path.exists(audio_path):
        return FileResponse(audio_path)
    # 음악 파일이 없어도 게임은 실행되도록 404 리턴
    return {"error": "Audio file not found"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

import json

from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    return FileResponse(path="public/index.html")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    counter = 0
    while True:
        counter += 1
        text = await websocket.receive_text()
        data = {
            "id": counter,
            "data": text,
        }
        json_string = json.dumps(data, indent=4)
        await websocket.send_json(json_string)
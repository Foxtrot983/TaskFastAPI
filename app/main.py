from typing import List

from fastapi import FastAPI, WebSocket, Depends
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session
from db import SessionLocal, engine
import models, schemas, crud


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def index():
    return FileResponse(path="../public/index.html")

@app.post("/post/", response_model=schemas.Data)
def create_data(data: schemas.Data, db: Session = Depends(get_db)):
    db_data = crud.create_data(db, data=data.data)
    return db_data


@app.get("/show/", response_model=List[schemas.Data])
async def get_data(db: Session = Depends(get_db)):
    data = crud.get_data(db)
    return data


@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket, db: Session = Depends(get_db)
    ):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        crud.create_data(db, data=data)
        await websocket.send_text(data)

from pydantic import BaseModel


class Data(BaseModel):
    data: str

    class Config:
        orm_mode = True

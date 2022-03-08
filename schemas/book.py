from pydantic import BaseModel


class BookInfo(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True

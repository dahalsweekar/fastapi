from pydantic import BaseModel


class Item(BaseModel):
    id: int
    title: str
    description: str | None = None
    owner_id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str
    # items: list[Item] = []

    class Config:
        orm_mode = True

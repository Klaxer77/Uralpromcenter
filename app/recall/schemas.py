from pydantic import BaseModel


class RecallList(BaseModel):
    id: int
    img: str
from pydantic import BaseModel


class ProgressList(BaseModel):
    id: int
    img: str
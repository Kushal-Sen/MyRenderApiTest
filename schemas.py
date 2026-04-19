from pydantic import BaseModel, Field


class NameCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)


class HelloResponse(BaseModel):
    id: int
    message: str

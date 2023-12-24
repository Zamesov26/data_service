from pydantic import BaseModel


class AnswerResponse(BaseModel):
    id: int
    text: str
    is_true: bool


class CreateAnswer(BaseModel):
    text: str
    is_true: bool

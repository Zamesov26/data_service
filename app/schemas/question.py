from typing import Optional, List

from pydantic import BaseModel

from app.schemas.answers import AnswerResponse, Answer


class QuestionResponse(BaseModel):
    id: int
    type: str
    img: Optional[str] = None
    text: str
    answers: list[AnswerResponse]


class CreateQuestion(BaseModel):
    type: str
    text: str
    answers: List[Answer]


class CreateQuestionWithAnswers(CreateQuestion):
    answers: list[Answer]

    def to_dict(self):
        res = super().to_dict()
        res['answers'] = [i.__dict__ for i in res['answers']]
        return res

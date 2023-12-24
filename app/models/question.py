from typing import Optional

from pydantic import BaseModel

from app.models.answers import AnswerResponse, CreateAnswer


class QuestionResponse(BaseModel):
    id: int
    type: str
    img: Optional[str] = None
    text: str
    answers: list[AnswerResponse]


class CreateQuestion(BaseModel):
    id: int
    type: str
    text: str

    def to_dict(self):
        res = self.__dict__
        return res


class CreateQuestionWithAnswers(CreateQuestion):
    answers: list[CreateAnswer]

    def to_dict(self):
        res = super().to_dict()
        res['answers'] = [i.__dict__ for i in res['answers']]
        return res

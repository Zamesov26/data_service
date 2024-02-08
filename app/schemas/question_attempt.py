from typing import List

from pydantic import BaseModel

from app.schemas.answers import Answer


class Attempt(BaseModel):
    attempt_id: int
    question_text: str
    question_type: str
    question_answers: List[Answer]

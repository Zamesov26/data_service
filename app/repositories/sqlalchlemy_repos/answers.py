from app.repositories.sqlalchlemy_repos.base import ISQLAlchemyRepo
from app.models import Answers


class AnswerRepo(ISQLAlchemyRepo):
    model = Answers

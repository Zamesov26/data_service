from app.repositories.sqlalchlemy_repos.base import ISQLAlchemyRepo
from app.models import Questionnaires


class QuestionnaireRepo(ISQLAlchemyRepo):
    model = Questionnaires

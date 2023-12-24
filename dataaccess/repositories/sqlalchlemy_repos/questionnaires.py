from dataaccess.repositories.sqlalchlemy_repos.base import ISQLAlchemyRepo
from dataaccess.models import Questionnaires


class QuestionnaireRepo(ISQLAlchemyRepo):
    model = Questionnaires

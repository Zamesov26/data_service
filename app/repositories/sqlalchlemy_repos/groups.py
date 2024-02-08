from app.repositories.sqlalchlemy_repos.base import ISQLAlchemyRepo
from app.models import Groups


class GroupRepo(ISQLAlchemyRepo):
    model = Groups

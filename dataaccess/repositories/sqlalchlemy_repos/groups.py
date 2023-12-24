from dataaccess.repositories.sqlalchlemy_repos.base import ISQLAlchemyRepo
from dataaccess.models import Groups


class GroupRepo(ISQLAlchemyRepo):
    model = Groups

from dataaccess.repositories.sqlalchlemy_repos.base import ISQLAlchemyRepo
from dataaccess.models import Users


class UserRepo(ISQLAlchemyRepo):
    model = Users

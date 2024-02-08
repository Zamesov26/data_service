from app.repositories.sqlalchlemy_repos.base import ISQLAlchemyRepo
from app.models import Users


class UserRepo(ISQLAlchemyRepo):
    model = Users

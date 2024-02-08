from sqlalchemy import select

from app.repositories.abstract_repos import IAPIKeysRepository
from app.repositories.sqlalchlemy_repos.base import ISQLAlchemyRepo
from app.models import APIKeys


class APIKeysRepo(ISQLAlchemyRepo, IAPIKeysRepository):
    model = APIKeys

    async def check_key(self, key: str):
        stmt = select(self.model).filter_by(key=key)
        return bool((await self.session.execute(stmt)).scalar())


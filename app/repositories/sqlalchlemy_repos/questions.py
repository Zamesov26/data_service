from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.repositories.abstract_repos import IQuestionRepository
from app.repositories.sqlalchlemy_repos.base import ISQLAlchemyRepo
from app.models import Questions


class QuestionRepo(ISQLAlchemyRepo, IQuestionRepository):
    model = Questions

    async def find_all_with_answer(self, **filters):
        stmt = select(self.model).filter_by(**filters).options(
            selectinload(self.model.answers))
        result = await self.session.execute(stmt)
        return result.scalars().all()

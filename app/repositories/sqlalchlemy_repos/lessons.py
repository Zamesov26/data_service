from sqlalchemy import delete

from app.models import Lessons
from app.models import lesson_question_association

from app.repositories.abstract_repos import ILessonRepository
from app.repositories.sqlalchlemy_repos.base import ISQLAlchemyRepo


class LessonRepo(ISQLAlchemyRepo, ILessonRepository):
    model = Lessons

    async def delete_question(self, question_id):
        stmt = delete(lesson_question_association).filter_by(
            question_id=question_id)
        await self.session.execute(stmt)


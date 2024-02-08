from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models import UserAttempts, Users, Questions
from app.utils.unitofwork import IUnitOfWork


class AttemptService:
    @classmethod
    async def get_by_tg_id(cls, uow: IUnitOfWork, tg_id):
        async with uow:
            # TODO Добавить фильтр чтобы получать только актуальные вопросы
            stmt = select(UserAttempts.id, Questions.text, Questions.type,
                          Questions.answers) \
                .select_from(UserAttempts) \
                .join(Questions, UserAttempts.question_id == Questions.id) \
                .join(Users, UserAttempts.user_id == Users.id) \
                .filter(Users.telegram_id == tg_id) \
                .options(selectinload(Questions.answers)) \
                .limit(1)

            res = await uow.session.execute(stmt)
            return res.scalars().one_or_none()

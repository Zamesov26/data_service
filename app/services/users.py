from typing import Optional

from app.models import Users
from app.utils.unitofwork import IUnitOfWork


class UserService:
    @classmethod
    async def get_all(cls, uow: IUnitOfWork):
        async with uow:
            return await uow.users.find_all()

    @classmethod
    async def get_by_id(cls, uow: IUnitOfWork, user_id) -> Optional[Users]:
        async with uow:
            return await uow.users.find_one(id=user_id)

    @classmethod
    async def get_by_tg_id(cls, uow: IUnitOfWork, tg_id) -> Optional[Users]:
        async with uow:
            return await uow.users.find_one(telegram_id=tg_id)

    @classmethod
    async def create(cls, uow: IUnitOfWork,
                     tg_id, user_name) -> Optional[Users]:
        async with uow:
            res = await uow.users.add_one(telegram_id=tg_id, name=user_name)
            await uow.add(res)
            await uow.commit()
            return res

    @classmethod
    async def delete(cls, uow: IUnitOfWork, user_id):
        async with uow:
            await uow.users.delete_one(id_=user_id)
            await uow.commit()

    @classmethod
    async def delete_all(cls, uow: IUnitOfWork, user_ids: list[int]):
        async with uow:
            for user_id in user_ids:
                await uow.users.delete_one(id_=user_id)
            await uow.commit()

from app.utils.unitofwork import IUnitOfWork


class APIKeyService:
    @classmethod
    async def create_key(cls, uow: IUnitOfWork):
        async with uow:
            res = await uow.api_keys.add_one()
            await uow.add(res)
            await uow.commit()
            return res

    @classmethod
    async def check_key(cls, uow: IUnitOfWork, api_key) -> bool:
        async with uow:
            res = await uow.api_keys.check_key(key=api_key)
            return res

from app.utils.unitofwork import IUnitOfWork


class CourseService:
    @classmethod
    async def get_all(cls, uow: IUnitOfWork):
        async with uow:
            res = await uow.cour
            await uow.add(res)
            await uow.commit()
            return res

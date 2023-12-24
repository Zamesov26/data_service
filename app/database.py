from dataaccess.utils.unitofwork import SqlAlchemyUnitOfWork, IUnitOfWork


def get_uow() -> IUnitOfWork:
    return SqlAlchemyUnitOfWork()

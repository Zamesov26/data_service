from dataaccess.repositories.sqlalchlemy_repos.base import ISQLAlchemyRepo
from dataaccess.models import FSMData, FSMState


class FSMDataRepo(ISQLAlchemyRepo):
    model = FSMData


class FSMStateRepo(ISQLAlchemyRepo):
    model = FSMState

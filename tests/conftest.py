import pytest
from httpx import AsyncClient

from app import app as fastapi_app
from app.config import settings
from data_access import Base, engine
from app.utils import SqlAlchemyUnitOfWork


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="function")
async def uow():
    uow = SqlAlchemyUnitOfWork()
    yield uow

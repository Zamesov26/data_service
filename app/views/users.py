from fastapi import APIRouter, Depends

from app.utils.uow import get_uow
from app.services import UserService

router = APIRouter()


@router.get('/users')
async def get_users(uow=Depends(get_uow)):
    users = await UserService.get_all(uow)
    return 'user template'

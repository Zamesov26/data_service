from fastapi import APIRouter, Depends

from app.database import get_uow
from dataaccess.services import UserService

router = APIRouter()


@router.get('/users')
async def get_users(uow=Depends(get_uow)):
    users = await UserService.get_all(uow)
    return 'users templates'

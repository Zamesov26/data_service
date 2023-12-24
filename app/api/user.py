from fastapi import APIRouter, Depends

from app.database import get_uow
from app.models.users import UserResponse, UserCreate, UserDelete
from dataaccess.services import UserService

router = APIRouter()


@router.get('/users', response_model=list[UserResponse])
async def get_users(uow=Depends(get_uow)):
    users = await UserService.get_all(uow)
    return users


@router.post('/user/add', status_code=201, response_model=UserResponse)
async def add_user(user=Depends(UserCreate), uow=Depends(get_uow)):
    user = await UserService.create(uow, user.id, user.name)
    return user


@router.post('/user/del', status_code=204)
async def del_user(user=Depends(UserDelete), uow=Depends(get_uow)):
    await UserService.delete(uow, user.id)


@router.post('/user/del_many', status_code=204)
async def del_many(users: list[UserDelete], uow=Depends(get_uow)):
    user_ids = [user.id for user in users]
    await UserService.delete_all(uow, user_ids)

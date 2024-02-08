from typing import Union

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.utils.uow import get_uow
from app.services import UserService

router = APIRouter()


class NewUserAPI(BaseModel):
    telegram_id: int
    user_name: Union[str, None] = None


@router.post('/new_user')
async def new_user(user_info: NewUserAPI, uow=Depends(get_uow)):
    user = await UserService().get_by_tg_id(uow,
                                            str(user_info.telegram_id))
    if user:
        return JSONResponse(status_code=409,
                            content={
                                'status': 'Conflict',
                                'message': 'The user already exists'
                            })

    user = await UserService().create(uow,
                                      tg_id=str(user_info.telegram_id),
                                      user_name=user_info.user_name)
    return JSONResponse(status_code=201,
                        content={
                            'status': 'Created',
                            'message': 'User has been created'
                        })
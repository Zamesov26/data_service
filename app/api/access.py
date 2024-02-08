import asyncio

from fastapi import APIRouter, Depends

from app.middleware.api_key_checker import api_key_checker

router = APIRouter()


@router.get('/check_key', dependencies=[Depends(api_key_checker)])
async def check_key():
    await asyncio.sleep(2)
    return 'there is access'

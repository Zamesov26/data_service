from fastapi import Depends, HTTPException
from fastapi.security import APIKeyQuery, APIKeyHeader

from app.utils.uow import get_uow
from app.services.apikey import APIKeyService
from app.utils.unitofwork import IUnitOfWork


async def api_key_checker(
        api_key_query: str = Depends(APIKeyQuery(name="apikey",
                                                 auto_error=False)),
        api_key_header: str = Depends(APIKeyHeader(name="X-API-Key",
                                                   auto_error=False)),
        uow: IUnitOfWork = Depends(get_uow)
):
    api_key = api_key_query or api_key_header
    if api_key is None or not await APIKeyService.check_key(uow, api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key

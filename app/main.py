from typing import Optional

from fastapi import FastAPI, Depends

from app.html import user_router
from app.api import user_api_router
from app.api import quiz_api_router

app = FastAPI()
app.include_router(user_router)

app.include_router(user_api_router, prefix='/api', tags=["users"])
app.include_router(quiz_api_router, prefix='/api', tags=["quizzes"])


# class HotelsSearchArgs:
#     def __init__(
#             self,
#             location: int = 10,
#             has_spa: Optional[bool] = None,
#     ):
#         self.location = location
#         self.has_spa = has_spa
#
#
# @app.get('/')
# def get_hotels(
#         search_arg: HotelsSearchArgs = Depends()
# ):
#     return search_arg

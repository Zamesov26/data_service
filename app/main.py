from fastapi import FastAPI

from app.views import question_router
from app.views import course_router

from app.api import user_api_router
from app.api import quiz_api_router
from app.api import access_api_router

app = FastAPI()
app.include_router(question_router)
app.include_router(course_router)

app.include_router(access_api_router, prefix='/api', tags=["access"])
app.include_router(user_api_router, prefix='/api', tags=["users"])
app.include_router(quiz_api_router, prefix='/api', tags=["quizzes"])

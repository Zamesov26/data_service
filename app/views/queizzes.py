from fastapi import APIRouter, Depends

from app.utils.uow import get_uow
from app.services import QuizService

router = APIRouter()


@router.get('/quizzes')
async def get_users(uow=Depends(get_uow)):
    all_questions = await QuizService.get_all(uow)
    return all_questions

from fastapi import APIRouter, Depends

from app.database import get_uow
from app.models.question import QuestionResponse, CreateQuestion, \
    CreateQuestionWithAnswers
from dataaccess.services.quizzes import QuizService

router = APIRouter()


@router.get('/quizzes', response_model=list[QuestionResponse])
async def get_quizzes(uow=Depends(get_uow)):
    questions = await QuizService.get_all_with_answers(uow)
    return questions


@router.post('/quiz/add')
async def add_quiz(question: CreateQuestionWithAnswers, uow=Depends(get_uow)):
    await QuizService.add_with_answer(uow, question.to_dict())
    # print(question.to_dict())


# @router.post('/quizzes/add')
# async def add_quizzes(questions: list[CreateQuestion], uow=Depends(get_uow)):
#
#     # questions = await QuizService.add_with_answer(uow)
#     print(questions)

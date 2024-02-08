from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.middleware.api_key_checker import api_key_checker
from app.services.user_attempt import AttemptService
from app.utils.uow import get_uow

router = APIRouter()


@router.get(
    '/get_question/{user_tg_id}',
    dependencies=[Depends(api_key_checker)],
    # response_model=Attempt
)
async def get_question(user_tg_id, uow=Depends(get_uow)):
    print(await AttemptService.get_by_tg_id(uow, user_tg_id))
    single_data = {'question_answer_id': 1,
                   'text': 'some text',
                   'answers': [{'text': 'adssadff', 'is_true': False},
                               {'text': 'asdf', 'is_true': True},
                               {'text': 'asdf True', 'is_true': False}],
                   'type': 'single'}
    multiple_data = {'question_answer_id': 1,
                     'text': 'some text',
                     'answers': [{'text': 'adssadff', 'is_true': False},
                                 {'text': 'asdf True', 'is_true': True},
                                 {'text': 'asdf', 'is_true': False},
                                 {'text': 'фываэ True', 'is_true': True}],
                     'type': 'multiple'}
    open_ended_data = {'question_answer_id': 1,
                       'text': 'some text',
                       'answers': [],
                       'type': 'open-ended'}
    return JSONResponse(content=multiple_data)


@router.post(
    '/send_answer/{user_tg_id}/{question_answer_id}',
    dependencies=[Depends(api_key_checker)],
    # response_model=Attempt
)
async def send_answer(user_tg_id, question_answer_id, uow=Depends(get_uow)):
    return 'Ok'

from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from app.schemas.question import CreateQuestion

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/course/{course_id}/lesson/{lesson_id}/create_question",
            response_class=HTMLResponse)
async def create_question_form(course_id, lesson_id, request: Request):
    return templates.TemplateResponse("create_question.html",
                                      {"request": request,
                                       'course_id': course_id,
                                       'lesson_id': lesson_id})


@router.post("/course/{course_id}/lesson/{lesson_id}/create_question")
async def create_question(course_id, lesson_id, data: CreateQuestion):
    print(dict(data))
    return data

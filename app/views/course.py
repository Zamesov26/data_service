from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.utils.uow import get_uow

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get('/courses/new_course')
async def get_courses(request: Request):
    return templates.TemplateResponse("create_course.html",
                                      {"request": request})


@router.get('/courses')
async def get_courses(uow: Depends(get_uow), request: Request):

    return templates.TemplateResponse("list_courses.html",
                                      {"request": request})

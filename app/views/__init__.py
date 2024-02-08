__all__ = [
    'user_router',
    'quiz_router',
    'question_router',
    'course_router'
]

from app.views.users import router as user_router
from app.views.question import router as question_router
from app.views.queizzes import router as quiz_router
from app.views.course import router as course_router

__all__ = [
    'user_api_router',
    'quiz_api_router',
    'access_api_router',
]


from app.api.quize import router as user_api_router
from app.api.user import router as quiz_api_router
from app.api.access import router as access_api_router

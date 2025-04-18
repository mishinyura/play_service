from fastapi import FastAPI
from app.api.user import user_router

ROUTES = {
    '': user_router
}

app = FastAPI()


def set_routes(app: FastAPI):
    """Устанавливает в приложение ручки"""
    for prefix, router in ROUTES.items():
        app.include_router(router=router, prefix=prefix)


def get_app():
    """Создает приложение и возвращает уже настроенный экземпляр"""
    app = FastAPI(title='Play Service')
    set_routes(app)
    return app

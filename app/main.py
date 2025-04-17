import uvicorn
import asyncio

from app.core.app import get_app
from app.core.config import settings
from app.core.db import create_tables


if __name__ == '__main__':
    asyncio.run(create_tables())
    app = get_app()
    app.mount(settings.app.app_mount, app)

    uvicorn.run(app, host='localhost', port=8080)
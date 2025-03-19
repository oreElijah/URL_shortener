from fastapi import FastAPI
from contextlib import asynccontextmanager

from database.config import connect_db, disconnect_db
from routers.url_shortener import router as url_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await disconnect_db()

app = FastAPI(lifespan=lifespan)

app.include_router(url_router, prefix="/api/v1/url")
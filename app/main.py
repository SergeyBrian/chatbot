from fastapi import FastAPI
from app.routers import chat, categories

app = FastAPI(prefix="/api")
app.include_router(chat.router)
app.include_router(categories.router)

from fastapi import FastAPI
from app.routers import chat, categories, questions, user

app = FastAPI(prefix="/api")
app.include_router(chat.router)
app.include_router(categories.router)
app.include_router(questions.router)
app.include_router(user.router)

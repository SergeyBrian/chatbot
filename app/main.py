from fastapi import FastAPI
from app.routers import chat

app = FastAPI()
app.mount("/api", chat.router)

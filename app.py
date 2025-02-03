# coding=utf-8

from fastapi import FastAPI
from routes.user.funcs import user_router

# Initialize app
app = FastAPI(
    title="Messenger API",
    description="A real-time messaging application built with FastAPI.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


# Users
app.include_router(user_router)


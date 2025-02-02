# coding=utf-8

from fastapi import FastAPI
from routes.user.funcs import user_router

# Initialize app
app = FastAPI()


app.include_router(user_router, prefix="/api", tags=["Users"])


# Create base route
@app.get("/")
def read_root():
    return {"message": "Messenger API is running"}


# coding=utf-8

from fastapi import FastAPI

# Initialize app
app = FastAPI()


# Create base route
@app.get("/")
def read_root():
    return {"message": "Messenger API is running"}


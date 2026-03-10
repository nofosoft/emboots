import os

from fastapi import FastAPI
from scheduler import start_scheduler
from contextlib import asynccontextmanager
from dotenv import load_dotenv

load_dotenv()   # membaca file .env


@asynccontextmanager
async def lifespan(app: FastAPI):

    # start scheduler
    start_scheduler()

    yield

    # shutdown event (optional)
    print("Application shutting down")

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI()

@app.post('/upload')
async def upload_file(
    file: UploadFile = File(...), # recieve file upload endpoint
    caption: str = Form(''),
    session: AsyncSession = Depends(get_async_session)
):
    pass
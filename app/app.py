from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI()

text_posts = {1: {'title': 'New Post', 'content': 'Cool test post'},
              2: {'title': 'Python Tip', 'content': 'Use list comprehensions for cleaner loops.'},
              3: {'title': 'Daily Motivation', 'content': 'Consistency beats intensity every time.'},
              4: {'title': 'Fun Fact', 'content': 'The first computer bug was an actual moth found in a Harvard Mark II.'},
              5: {'title': 'Update', 'content': 'Just launched my new project! Excited to share more soon.'},
              6: {'title': 'Tech Insight', 'content': 'Async IO in Python can massively speed up I/O-bound tasks.'},
              7: {'title': 'Quote', 'content': "'Programs must be written for people to read, and only incidentally for mach"}}
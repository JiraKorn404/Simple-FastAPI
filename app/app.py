from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {1: {'title': 'New Post', 'content': 'Cool test post'},
              2: {'title': 'Python Tip', 'content': 'Use list comprehensions for cleaner loops.'},
              3: {'title': 'Daily Motivation', 'content': 'Consistency beats intensity every time.'},
              4: {'title': 'Fun Fact', 'content': 'The first computer bug was an actual moth found in a Harvard Mark II.'},
              5: {'title': 'Update', 'content': 'Just launched my new project! Excited to share more soon.'},
              6: {'title': 'Tech Insight', 'content': 'Async IO in Python can massively speed up I/O-bound tasks.'},
              7: {'title': 'Quote', 'content': "'Programs must be written for people to read, and only incidentally for mach"}}

@app.get('/posts')
def get_all_post(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get('/posts/{id}')
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail='Post not found')

    return text_posts.get(id)

@app.post('/posts')
def create_post(post: PostCreate) -> PostResponse:
    new_post = {'title': post.title, 'content': post.content}
    text_posts[max(text_posts.keys()) + 1 ] = new_post
    return new_post


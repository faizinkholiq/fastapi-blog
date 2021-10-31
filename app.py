from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime

app = FastAPI()

postdb = []

#post model
class Post(BaseModel):
    id: int
    title: str
    content: Text
    created_ay: datetime = datetime.now()
    published: Optional[bool] = False

@app.get("/")
def read_root():
    return {"home": "Home Page"}


@app.get("/blog")
def get_posts():
    return postdb

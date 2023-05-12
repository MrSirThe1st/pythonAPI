from typing import Optional, Union
from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None




my_posts = [{"title": "title post 1", "content":"content post 1", "id": "id"}, {"title": "favourite food", "content": "i like pizza", "id": "1"}]


@app.get("/")
def get_posts():
    return{"data":my_posts}


@app.post("/posts")
def create_posts(post : Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append()
    return {"data": post_dict}

 
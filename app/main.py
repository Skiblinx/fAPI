from random import randrange
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
  title: str
  content: str
  draft: bool = False 


my_posts = [
  {"title": "post title","content": "content of post", "id": 1},
  {"title": "Favorite food","content": "Cheese Pizza", "id": 2},
  ]

def find_post(id):
  for p in my_posts:
    if p["id"] == id:
      return p

def find_index(id):
  for i, p in enumerate(my_posts):
    if p["id"] == id:
      return i

@app.get('/posts')
async def root():
  return{"Data": my_posts}


# This is creating a post without any form of validation
@app.post('/posts')
#  async def create_post(payload: dict = Body(...) ):
#   print(payload)
#   return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}

# Creating a post with a validation using Pydantic Model to validate a schema.
@app.post('/posts/create/')
async def create_post(posts: Post):
  posts_dict = posts.dict()
  posts_dict['id'] = randrange(0, 100000000)
  my_posts.append(posts_dict)

  return {"data": posts} 

@app.get('/posts/{id}')
async def get_post(id: int, response: Response): 
  post = find_post(id)
  if not post: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
  return {"Data": post}

@app.delete('/posts/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
  post_index = find_index(id)
  if post_index == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
  my_posts.pop(post_index)
  return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/update/{id}')
def update_post(id: int, post: Post):

  post_index = find_index(id)
  if not post_index:
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Post with id: {id} not found")
  post_dict = post.model_dump()
  print(post_dict)
  post_dict["id"] = id
  my_posts[post_index] = post

  return{"message": "Post updated successfully", "data": post}
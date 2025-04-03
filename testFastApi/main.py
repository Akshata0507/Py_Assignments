from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

# Model for user
class User(BaseModel):
    id: int
    name: str

# In-memory data storage
users = [
    User(id=1, name='Alice'),
    User(id=2, name='Bob')
]

# Get all users
@app.get("/users", response_model=List[User])
def get_users():
    return users

# Get user by ID
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if user:
        return user
    return {"message": "User not found"}

# Create a new user
@app.post("/users", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)













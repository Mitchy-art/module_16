from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(
        username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
        age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:
    cur_id = str(int(max(users, key=int)) + 1)
    users[cur_id] = f'Имя: {username}, возраст: {age}'
    return f"User {cur_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: str = Path(description='Enter user ID', example='1'),
        username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
        age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: str = Path(description='Enter user ID', example='2')) -> str:
    users.pop(user_id)
    return f'The user {user_id} is deleted'
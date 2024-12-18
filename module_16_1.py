from fastapi import FastAPI

app = FastAPI()


@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user")
async def user_name_age(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


@app.get('/user/{user_id}')
async def id_user(user_id: int) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get("/")
async def main() -> str:
    return 'Главная страница'

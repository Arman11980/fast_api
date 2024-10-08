from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def new():
    return {"message": "hello world"}

@app.get("/user/admin")
async def new_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def new_id(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/new_user")
async def new_name(username: str = "Alex", age: int = 24): # по умолчанию не работают параметры почему то(всё в ручную)
    return {"mssage": f"Информация о пользователе.Имя: {username}, Возраст: {age}"}
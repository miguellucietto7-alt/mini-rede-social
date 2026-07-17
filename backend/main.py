from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    nome: str
    senha: str
    idade: int



database: list = {
    "users": [],
    "id": 1,
}


@app.post("/create_user")
def create_user(user: User):
    new_user = {
        "id": database["id"],
        "nome": user.nome,
        "senha": user.senha,
        "idade": user.idade,
    }
    database["users"].append(new_user)
    database["id"] += 1

    return new_user


@app.get("/users")
def get_users():
    return database["users"]


@app.get("/user/{id}")
def get_user(id: int):
    for user in database["users"]:
        if user["id"] == id:
            return user
    return f"user with id {id} not found"

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List

user = APIRouter()
users: List['model_user'] = []

# User model
class model_user(BaseModel):
    id: str
    usuario: str
    contrasena: str
    created_at: datetime = datetime.now()
    estatus: bool = False

# Person Model
class model_person(BaseModel):
    id: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    titulo_cortesia: str
    fecha_nacimiento: str
    genero: str
    tipo_sangre: str


@user.get("/")
def bienvenida():
    return "Bienvenido al sistema de apis"

@user.get("/users", tags=["Usuarios"])
def get_usuarios():
    return users

@user.post("/users", tags=["Usuarios"])
def save_usuarios(insert_users: model_user):
    users.append(insert_users)
    return "Datos guardados"

@user.put("/users/{user_id}", tags=["Usuarios"])
def update_usuario(user_id: str, updated_user: model_user):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": "Usuario actualizado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@user.delete("/users/{user_id}" , tags=["Usuarios"])
def delete_usuario(user_id: str):
    for index, user in enumerate(users):
        if user.id == user_id:
            del users[index]
            return {"message": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

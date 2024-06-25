from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

person = APIRouter()
persons: List['model_person'] = []

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

@person.get("/persons", tags=["Personas"])
def get_personas():
    return persons

@person.post("/persons", tags=["Personas"])
def save_personas(insert_person: model_person):
    persons.append(insert_person)
    return "Datos guardados"

@person.put("/persons/{person_id}", tags=["Personas"])
def update_persona(person_id: str, updated_person: model_person):
    for index, user in enumerate(persons):
        if user.id == person_id:
            persons[index] = updated_person
            return {"message": "Usuario actualizado"}
    raise HTTPException(status_code=404, detail="Persona no encontrado")

@person.delete("/persons/{person_id}" , tags=["Personas"])
def delete_persona(person_id: str):
    for index, person in enumerate(persons):
        if person.id == person_id:
            del persons[index]
            return {"message": "Persona eliminada"}
    raise HTTPException(status_code=404, detail="Persona no encontrada")
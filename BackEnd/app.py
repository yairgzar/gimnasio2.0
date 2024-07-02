from fastapi import FastAPI
from routes.user import user 
from routes.persona import person 

app=FastAPI(
    title="Gimnasio S.A. de C.V.",
    description="API para el almacenamiento de información de un gimnasio"
)
app.include_router(user)
app.include_router(person)
print ("Hola bienvenido a mi backend")
from fastapi import FastAPI
from typing import Optional
from consultas import Estudiante

app = FastAPI()

#Peticiones a estudiantes
@app.get("/estudiante/{correo}")
def consulta_estudiante(correo: str):
    consulta = Estudiante()
    return {"tipo": "peticion get", "correo": correo, "cursos": consulta.consultar_evaluaciones()}

#Peticiones a profesores
@app.get("/profesor")
def consulta_profesor():
    return {"tipo": "peticion get"}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/prueba")
def peticion_prueba():
    return {"nombre": "prueba", "clave1": "valor1"}
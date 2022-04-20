from fastapi import FastAPI, Depends
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from consultas import Estudiante

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#Peticiones a estudiantes
@app.get("/estudiante/{correo}")
def consulta_estudiante(correo: str, token: str = Depends(oauth2_scheme)):
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


@app.get("/test")
def read_root():
    return {"nombre": "prueba"}
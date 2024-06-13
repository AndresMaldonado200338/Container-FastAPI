from fastapi import FastAPI
from starlette.responses import RedirectResponse
from typing import Dict
import json

app = FastAPI()

with open("languages.json", "r", encoding="utf-8") as file:
    datos_idiomas = json.load(file)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

# Ruta para obtener todos los idiomas
@app.get("/idiomas/", response_model=Dict[int, str])
async def obtener_idiomas():
    return datos_idiomas

# Ruta para obtener un idioma por su ID
@app.get("/idiomas/{idioma_id}", response_model=str)
async def obtener_idioma_por_id(idioma_id: int):
    idioma = datos_idiomas.get(str(idioma_id))
    if idioma:
        return idioma
    else:
        return "Idioma no encontrado"
    
#Ruta para buscar el id de un idioma por su nombre
@app.get("/idiomas/buscar/{idioma_nombre}", response_model=str)
async def buscar_idioma_por_nombre(idioma_nombre: str):
    for idioma_id, idioma in datos_idiomas.items():
        if idioma_nombre.lower() in idioma.lower():
            return f"El id del idioma {idioma_nombre} es: {idioma_id}"
    return "Idioma no encontrado"

#Ruta para agregar un idioma en la lista
@app.post("/idiomas/agregar/{idioma_id}/{idioma_nombre}")
async def agregar_idioma(idioma_id: int, idioma_nombre: str):
    if str(idioma_id) in datos_idiomas or idioma_nombre in datos_idiomas.values():
        return "El idioma ya existe"
    if idioma_id < 0:
        return "El id del idioma no puede ser negativo"
    if not idioma_nombre.isalpha():
        return "El nombre del idioma solo puede contener letras"
    if not idioma_nombre.istitle():
        return "El nombre del idioma debe tener la primera letra en mayúscula"
    datos_idiomas[str(idioma_id)] = idioma_nombre
    return "Idioma agregado correctamente"

#Ruta para eliminar un idioma de la lista
@app.delete("/idiomas/eliminar/{idioma_id}")
async def eliminar_idioma(idioma_id: int):
    global datos_idiomas
    idioma = datos_idiomas.pop(str(idioma_id), None)
    if idioma:
        return "Idioma eliminado correctamente"
    else:
        return "Idioma no encontrado"
    
#Ruta para modificar el nombre de un idioma
@app.put("/idiomas/modificar/{idioma_id}/{idioma_nombre")
async def modificar_idioma(idioma_id: int, idioma_nombre: str):
    global datos_idiomas
    if str(idioma_id) not in datos_idiomas:
        return "Idioma no encontrado"
    if not idioma_nombre.isalpha():
        return "El nombre del idioma solo puede contener letras"
    if not idioma_nombre.istitle():
        return "El nombre del idioma debe tener la primera letra en mayúscula"
    datos_idiomas[str(idioma_id)] = idioma_nombre
    return "Idioma modificado correctamente"
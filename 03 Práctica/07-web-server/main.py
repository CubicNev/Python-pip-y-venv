"""
Main
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Mon 30-Dec-2024

Script principal de la aplicación
"""
import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Se crea una instancia de la aplicación
app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4]

@app.get('/contact/', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola!</h1>
        <p>Bienvenido.</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()
"""
Store
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Mon 30-Dec-2024

Se hacen peticiones a una API de ejemplo
"""

import requests

def get_categories():
    # Hace petición GET
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # Obtiene el esatado
    print(r.status_code)
    # Imprime lo obtenido
    print(r.text)
    print(type(r.text))

    # Respuesta en formato json para manejo de datos
    categories = r.json()
    for category in categories:
        print(category['name'])
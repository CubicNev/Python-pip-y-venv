# Solicitudes HTTP con Requests

En Python se usa la librería `requests` para hacer peticiones a servidores web desde Python. Se usa el ejemplo de [**Fake API**](https://fakeapi.platzi.com/), en el que podemos hacer peticiones como:

```json
[
  {
    "id": 1,
    "name": "Change title",
    "image": "https://i.imgur.com/QkIa5tT.jpeg",
    "creationAt": "2024-12-29T21:48:48.000Z",
    "updatedAt": "2024-12-30T00:09:17.000Z"
  },
  {
    "id": 2,
    "name": "Electronics",
    "image": "https://i.imgur.com/ZANVnHE.jpeg",
    "creationAt": "2024-12-29T21:48:48.000Z",
    "updatedAt": "2024-12-29T21:48:48.000Z"
  },
  {
    "id": 3,
    "name": "Change title",
    "image": "https://i.imgur.com/Qphac99.jpeg",
    "creationAt": "2024-12-29T21:48:48.000Z",
    "updatedAt": "2024-12-30T00:09:11.000Z"
  },
  {
    "id": 4,
    "name": "Shoes",
    "image": "https://i.imgur.com/qNOjJje.jpeg",
    "creationAt": "2024-12-29T21:48:48.000Z",
    "updatedAt": "2024-12-29T21:48:48.000Z"
  },
  {
    "id": 5,
    "name": "Miscellaneous",
    "image": "https://i.imgur.com/BG8J0Fj.jpg",
    "creationAt": "2024-12-29T21:48:48.000Z",
    "updatedAt": "2024-12-29T21:48:48.000Z"
  },
  {
    "id": 7,
    "name": "string",
    "image": "https://pravatar.cc/",
    "creationAt": "2024-12-29T22:03:00.000Z",
    "updatedAt": "2024-12-29T22:03:00.000Z"
  },
  {
    "id": 29,
    "name": "New Category yyy",
    "image": "https://placeimg.com/640/480/any",
    "creationAt": "2024-12-30T07:34:42.000Z",
    "updatedAt": "2024-12-30T07:34:42.000Z"
  },
  {
    "id": 31,
    "name": "Grosery",
    "image": "https://placeimg.com/640/480/any",
    "creationAt": "2024-12-30T11:01:28.000Z",
    "updatedAt": "2024-12-30T11:01:28.000Z"
  }
]
```

Se hace un request desde python hatsa este ENDPOINT o recurso que regresa una resuesta en `json`, que tiene un formato similar a una lista de diccionarios. En este caso, cada elemento representa una categoría de un comercio en línea. [1]

## Módulo `requests`

Nos permite hacer peticiones a otro servicio web. [2]

### Instalación

```sh
pip install requests
```

### Ejemplo de uso

```python
import requests

def get_categories():
    # Hace petición GET
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # Obtiene el esatado
    print(r.status_code)
    # Imprime lo obtenido
    print(r.text)
```

<!-- Referencias -->

[1]: <https://api.escuelajs.co/api/v1/categories> "Petición GET"
[2]: <https://requests.readthedocs.io/en/latest/> "Módulo Requests"

La salida obtenida es la siguiente:

```text
200
[{"id":1,"name":"Change title","image":"https://i.imgur.com/QkIa5tT.jpeg","creationAt":"2024-12-29T21:48:48.000Z","updatedAt":"2024-12-30T00:09:17.000Z"},{"id":2,"name":"Electronics","image":"https://i.imgur.com/ZANVnHE.jpeg","creationAt":"2024-12-29T21:48:48.000Z","updatedAt":"2024-12-29T21:48:48.000Z"},{"id":3,"name":"Change title","image":"https://i.imgur.com/Qphac99.jpeg","creationAt":"2024-12-29T21:48:48.000Z","updatedAt":"2024-12-30T00:09:11.000Z"},{"id":4,"name":"Shoes","image":"https://i.imgur.com/qNOjJje.jpeg","creationAt":"2024-12-29T21:48:48.000Z","updatedAt":"2024-12-29T21:48:48.000Z"},{"id":5,"name":"Miscellaneous","image":"https://i.imgur.com/BG8J0Fj.jpg","creationAt":"2024-12-29T21:48:48.000Z","updatedAt":"2024-12-29T21:48:48.000Z"},{"id":7,"name":"string","image":"https://pravatar.cc/","creationAt":"2024-12-29T22:03:00.000Z","updatedAt":"2024-12-29T22:03:00.000Z"},{"id":29,"name":"New Category yyy","image":"https://placeimg.com/640/480/any","creationAt":"2024-12-30T07:34:42.000Z","updatedAt":"2024-12-30T07:34:42.000Z"},{"id":31,"name":"Grosery","image":"https://placeimg.com/640/480/any","creationAt":"2024-12-30T11:01:28.000Z","updatedAt":"2024-12-30T11:01:28.000Z"},{"id":38,"name":"Categoria nova","image":"https://placeimg.com/640/480/any","creationAt":"2024-12-30T16:59:08.000Z","updatedAt":"2024-12-30T16:59:08.000Z"},{"id":39,"name":"Categoria nova","image":"https://placeimg.com/640/480/any","creationAt":"2024-12-30T17:02:52.000Z","updatedAt":"2024-12-30T17:02:52.000Z"},{"id":40,"name":"Categoria nova","image":"https://placeimg.com/640/480/any","creationAt":"2024-12-30T17:07:05.000Z","updatedAt":"2024-12-30T17:07:05.000Z"}]
```

> 📝 **Nota:** La respuesta se esta obteniendo y manejando unicamente en formato de texto, para manejar la información hay que tranformarlo.

```python
# Respuesta en formato json para manejo de datos
categories = r.json()
for category in categories:
    print(category['name'])
```

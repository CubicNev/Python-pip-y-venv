# Dockerizando web services

[◀️](./../README.md)

Docker no se usa tanto para correr solo scripts, se usa para tener un sistema un sistema encencido con cambios que se hacen en vivo para desarrollo web. De esta forma se tiene un servicio que se mantiene actualizado "al aire", y gracias a tenerlo en un contenedor es más fácil desplegarlo en la nube.

## Configuración

Se crea el `Dockerfile` similar al tema anterior, con la diferencia, de que la ultima línea se usa para lanzar el Servidor en FastAPI usando uvicorn.

```docker
FROM python:3.10

WORKDIR /app
COPY requirementes.txt /app/requirementes.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirementes.txt

COPY . /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

La ultima linea ejecuta la instrucción para ejecutar el servidor con uvicorn

```sh
uvicorn main:app --host 0.0.0.0 --port 80
```

> 📝 **Nota:** Se da como una lista de instrucciones.

Se crea el `docker-compose.yml`, agregandole un enlace entre los puertos (similar a como se hace enlace entre archivos). De tal forma que se enlaza el pueto 80 de la maquina local con el puerto del contenedor.

```yaml
services:
  web-server:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
    ports:
      - '80:80'
```

## Construcción del contenedor

- **Paso 1:** Dentro de la carpeta contenedora del proyecto ejecutamos `docker-compose build` para construirlo

```sh
docker-compose build
```

- **Paso 2:** Levantar el contenedor con `docker-compose up -d`

```sh
docker-compose up -d
```

- **Paso 3:** Verificar que el contenedor se haya ejecutado

```sh
docker-compose ps
```

> 📝 **Nota:** Ahora se puede ver que también se levantaron puertos.

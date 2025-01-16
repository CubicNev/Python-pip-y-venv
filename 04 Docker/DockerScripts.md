# Dockerizando Scripts

## Configuración del contenedor

En este caso, se dockerizara el proyecto "**app**". Para empezar, se crea un nuevo archivo llamado `Dockerfile` en la raíz. Con el siguiente contenido:

```docker
FROM python:3.8

WORKDIR /app
COPY requirementes.txt /app/requirementes.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirementes.txt

COPY . /app/

CMD bash -c "while true; do sleep 1; done"
```

> 📝 **Nota:** Las instrucciones en docker se escriben en mayúsculas.

Lo que hace el archivo es:

- `FROM` Le decimos a docker la versión de python de la que va a partir el ambiente.
- `WORKDIR` Crea el espacio de trabajo
- `COPY` Copia los archivos de las dependencias. Copia de local (izquierda) a el entorno (derecha).
- `RUN` Ejecuta la instruccion para instalar las dependencias.

> 📝 **Nota:** Las banderas `--no-cache-dir` (No aplica el cache) y `--upgrade` (Si hay una actualización del gestor de paquetes, la haga) se agregan por buenas prácticas.

- `COPY . /app/` Copia todos los archivos del proyecto al entorno
- `CMD bash -c "while true; do sleep 1; done"` mantiene encencido el contenedor con un ciclo infinito hecho en bash.

Para correr el contenedor se hace uso del archivo ``docker-compose.yml`, el cual declara cómo y desde dónde se inicializará el contenedor.

```yaml
services:
  app-csv:
    build:
      context: .
      dockerfile: Dockerfile
```

- Se define la etiqueta de servicios.
- Se da nombre al servicio (app-csv).
- Se agrega un build.
- Se da el contexto dentro de la carpeta actual.
- Se indica el dockerfile a leer

## Construyendo el contenedor (WSL)

- **Paso 1:** Encender Docker desde Windows (Abrir la ventana)
- **Paso 2:** En la terminal se ejecuta el comando `docker-compose build`

```sh
docker-compose build
```

> 📝 **Nota:** Hace la construcción del sistema siguiendo los pasos descritos en `Dockerfile`

- **Paso 3:** Lanzar el contenedor

```sh
docker-compose up -d
```

- **Paso 4:** Revisar el estado del contenedor (STATUS = running)

```sh
docker-compose ps
```

- **Paso 5:** Ingresar al ambiente `docker-compose exec <nombre-contenedor> <tipo-terminal>`

```sh
docker-compose exec app-csv bash
```

> 📝 **Nota:** Es como trebajar en un servidor Unix
>
> Para salir del contenedor se ingresa el comando `exit`

## Actualizar un contenedor después de hacer cambios

- **Paso 1:** Reconstruir el contenedor (Al hacer cambios)

```sh
docker-compose build
```

- **Paso 2:** Bajar el contenedor

```sh
docker-compose down
```

- **Paso 3:** Volver a levantar el contenedor

```sh
docker-compose up -d
```

- **Paso 4:** Revisa el estado del contenedor

```sh
docker-compose ps
```

- **Paso 5:** Ingresar al ambiente `docker-compose exec <nombre-contenedor> <tipo-terminal>`

```sh
docker-compose exec app-csv bash
```

## Automatizar la vinculación de archivos

Para mejorar la experiecnia de desarrollo, se enlaza el sistema de archivos con el que esta dentro del contenedor. Para que al momento de hacer cambios en el proyecto no se tenca que reconstruir todo el contenedor.

Para esto se edita la configuración. En `docker-compose.yml` se agrega la etiqueta `volumes`.

```yaml
services:
  app-csv:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
```

En `- .:/app` se da la instrucción:

- `-` "De este proyecto"
- `.` "Todos los archivos"
- `:` "Enlazalo directamente a..."
- `/app` "A la carpeta **/app**, que esta dentro del contenedor"

Al hacer este cambio no es necesario hacer un `build`, solo un `up -d`. Ya que solo se debe recrear el contenedor.

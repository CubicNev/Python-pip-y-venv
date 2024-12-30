# Curso de Python: PIP y Entornos Virtuales

Curso de Python 🐍 donde se ve funcionalidades de PIP (instalacion de dependencias) y entornos virtuales (aislamiento de proyectos para evitar conflictos entre módulos y sus versiones). Así como encapsulación de aplicaciones en contenedores de Docker.

Impartido por: Nicolas Molina @nicobytes
By: Platzi

## Contents

1. [Introduccion](./01%20Introduccion/)
    1. [Instalaciones](./01%20Introduccion/Instalaciones.md)
    2. [VSCode](./01%20Introduccion/VSCode.md)
    3. [Git y Github](./01%20Introduccion/Git%20y%20Github.md)
    4. [Flujo de Trabajo](./01%20Introduccion/Flujo%20de%20trabajo.md)
2. [PIP y Entornos Virtuales](./02%20PIP%20y%20Entornos%20Virtuales/)
    1. [¿Qué es pip?](./02%20PIP%20y%20Entornos%20Virtuales/pip.md)
    2. [Gráficas en Python con PIP](./02%20PIP%20y%20Entornos%20Virtuales/04-app/readme.md)
    3. [¿Qué es un ambiente virtual? (venv)](./02%20PIP%20y%20Entornos%20Virtuales/Ambientes%20Virtuales.md)
    4. [Archivos de requerimientos](./02%20PIP%20y%20Entornos%20Virtuales/Ambientes%20Virtuales.md)
3. [Práctica](./03%20Práctica/)
    1. [Solicitudes HTTP con Requests](./03%20Práctica/httprequests.md)
    2. [Pandas](./03%20Práctica/pandas.md)
    3. [Python para Backend: web server con FastAPI](./03%20Práctica/)
4. [Python en contenedores de Docker](./04%20Python%20en%20contenedores%20de%20Docker/)
    1. [¿Qué es Docker?](./04%20Python%20en%20contenedores%20de%20Docker/)
    2. [Instalacion de Docker](./04%20Python%20en%20contenedores%20de%20Docker/)
    3. [Docker para el día a día](./04%20Python%20en%20contenedores%20de%20Docker/)
    4. [Dockerizando web services](./04%20Python%20en%20contenedores%20de%20Docker/)

## Brief Introduction

El objetivo de este curso es trabajar con Python en un entorno profesional. Para esto se ve un breve repaso de algunos comandos que se pueden hacer en una terminal (con base Unix)

**pwd**: Indica en qué ubicación estamos

```sh
~$ pwd
/home/cubic/Learn/Python/Python-pip-y-venv
```

**mkdir**: Crear una nueva carpeta

```sh
~$ mkdir "01 Introduccion"
```

**ll**: Lista de archivos con cierto formato (es un alias)

```sh
~$ ll
total 40
drwxr-xr-x 1 cubic cubic  4096 Dec  5 11:56 '01 Introduccion'/
drwxr-xr-x 1 cubic cubic  4096 Dec  5 11:56 '02 PIP y Entornos Virtuales'/
drwxr-xr-x 1 cubic cubic  4096 Dec  5 11:56 '03 Práctica'/
drwxr-xr-x 1 cubic cubic  4096 Dec  5 11:56 '04 Python en contenedores de Docker'/
-rw-r--r-- 1 cubic cubic 35149 Dec  5 11:21  LICENSE
-rw-r--r-- 1 cubic cubic  2253 Dec  5 12:10  README.md
```

**cd**: Nos permite abrir una carpeta

```sh
~$ cd "01 Introduccion"
~/01 Introduccion$
```

**clear**: Nos permite despejar la terminal

```sh
~$ clear
```

**git init**: Inicializar un repositorio de git

```sh
~$ git init
Initialized empty Git repository in /home/Python-pip-y-venv/.git/
```

**touch**: Crear archivos

```sh
~$ touch README.md
```

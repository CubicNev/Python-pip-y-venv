# Instalaciones para el curso

## Windows (WSL) y Linux

Se buscará instalar python. Normalmente WSL y Linux ya tienen instalado python por defecto, se puede ver si esta instalado usando el comando `python`, o bien, el comando `python3`. *i.e.*

```sh
~$ python
zsh: command not found: python

~$ python3
Python 3.10.12 (main, Nov  6 2024, 20:22:13) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit() #para salir de la interfaz de python
```

> 📝 **Nota:** En este ejemplo muestra que la palabra clave asociada a python es python3

El comando ejecuta python y permite usar las funcionalidades y operaciones de python.

### Instalación

En caso que python no este instalado, se pueden usar los siguientes comandos:

1: `apt update` para actualizar los paquetes.

```sh
~$ apt update
E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)
E: Unable to lock directory /var/lib/apt/lists/
W: Problem unlinking the file /var/cache/apt/pkgcache.bin - RemoveCaches (13: Permission denied)
W: Problem unlinking the file /var/cache/apt/srcpkgcache.bin - RemoveCaches (13: Permission denied)
```

Este comando necesita ser ejecutado con permisos de superusuario por lo que se usa el coamndo `sudo` *i.e.* `sudo apt update`

```sh
~$ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:3 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:4 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease
Hit:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
```

> ⚠️ **Cuidado:** Al usar `sudo` se pedira la ocntraseña del usaurio

Una vez hecho el update hacemos un upgrade con `sudo apt -y upgrade`

```sh
~$ sudo apt -y upgrade
```

### Verificar Instalación de python

Ahora podemos verificar que python este correctamente instalado con el siguiente comando con el cual verificamos la version usada.

```sh
~$ python3 -V
Python 3.10.12
```

### Instalación de gestor de paquetes de dependencias

Es necesario ver que este instalado el gestor de paquetes de dependencias (Que usaremos más adelante)

```sh
~$ sudo apt install -y python3-pip
```

### Verificar Instalación del gestor

```sh
~$ pip3 -V
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```

### Dependencias en entorno profesional

Necesitamos algunas dependencias utiles para desarrollo con python.

```sh
~$ sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

Los paquetes que se están importando sirven para proporcionar herramientas y funcionalidades necesarias para compilar y desarrollar software en el sistema

- **build-essential** ➡️ es un paquete que incluye herramientas de compilación y desarrollo de software necesarias para construir programas en C y C++

- **libssl-dev** ➡️ es el desarrollo de la biblioteca OpenSSL, que proporciona funcionalidades de seguridad para aplicaciones de red, como cifrado, autenticación y verificación de certificados

- **ibffi-dev** ➡️ es el desarrollo de la biblioteca libffi, que permite a las aplicaciones invocar funciones de otros programas en tiempo de ejecución

- **python3-dev** ➡️ es el paquete de desarrollo de Python 3, que incluye los archivos de cabecera y otras herramientas necesarias para compilar módulos y aplicaciones de Python

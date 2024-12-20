# ¿Qué es `pip`?

El ecosistema de python consiste en las principales librerias y frameworks que podemos usar para hacer nuestros proyectos. Todos los paquetes se pueden encontrar en el gestor de paquetes de python (*PIP*, *Package Installer for Pýthon*), la página para consultar todos los paquetes es *Python Package Index* (**PyPI** [1]), en ella se puede ver información de los paquetes como:

- Última versión
- Comando de instalación
- Documentación de la librería

Por ejemplo, para **matplotlib** [2], se observa que la versión (a la fecha de hoy) es la 3.10.0 y que el comando para instalar esta librería es

```sh
pip install matplotlib
```

## Uso de `pip`

Viene instalado por defecto con Python. Para comprobar que este instalado (en este caso para WSL), se usa:

```sh
pip3 -V
# out: pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```

## Ejercicio

Se crea la carpeta [`03-charts`](./03-charts/), y dentro de esta se instala el paquete *matplotlib*.

```sh
pip3 install matplotlib
```

Tras la instalación muestra el arbol de dependencias del paquete, entre ellas, por ejemplo, esta *numpy*.

Para ver qué librerías estan instaladas se usa:

```sh
pip3 freeze
```

Describe el entorno de python *en general*, de toda la computadora. No del proyecto en específico, si no del python global de la computadora.

<!-- Referencias -->

[1]: <https://pypi.org/> "Python Package Index"
[2]: <https://pypi.org/project/matplotlib/> "Matplotlib"

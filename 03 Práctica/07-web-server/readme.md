# Web Server

[◀️](./../../README.md)

## Configuración de ambiente de desarrollo

**Paso 1**: Inicializar un ambiente virtual dentro del proyecto

```sh
cd "03 Práctica/07-web-server"
python3 -m venv <Nombre del ambiente virtual>
```

> 📝 **Nota:** Se recomienda nombrar el ambiente virtual como **venv**

```sh
python3 -m venv venv
```

**Paso 2**: Activar el ambiente virtual

```sh
source venv/bin/activate
```

**Paso 3**: Instalar dependencias

```sh
pip3 install -r requirements.txt
```

## Ejecutar servicio

```sh
fastapi dev main.py
```

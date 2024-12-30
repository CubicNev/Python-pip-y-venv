# Web Server

[◀️](./../../README.md)

## Configuración de ambeinte de desarrollo

**Paso 1**: Inicializar un ambiente virtual dentro del proyecto

```sh
cd "02 PIP y Entornos Virtuales/04-app"
python3 -m venv <Nombre del ambiente virtual>
```

> 📝 **Nota:** Se recomienda nombrar el ambiente virtual como **env**

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

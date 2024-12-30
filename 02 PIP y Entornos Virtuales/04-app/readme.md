# Gráficar la población de un país

[◀️](./../../README.md)

A partir de la información de [`data.csv`](./data.csv). Gráficar la información de un país.

- Seleccionar solo la información poblacional, ignorando todo lo demás.
- Permitir ver el crecimiento poblacional del país a traves de los años con un **Bar Chart**

## Configuración de ambiente de desarrollo

**Paso 1**: Inicializar un ambiente virtual dentro del proyecto

```sh
cd "02 PIP y Entornos Virtuales/04-app"
python3 -m venv <Nombre del ambiente virtual>
```

> 📝 **Nota:** Se recomienda nombrar el ambiente virtual como **env**

```sh
python3 -m venv env
```

**Paso 2**: Activar el ambiente virtual

```sh
source env/bin/activate
```

**Paso 3**: Instalar dependencias

```sh
pip3 install -r requirements.txt
```

## Ejecución

```sh
cd "02 PIP y Entornos Virtuales/04-app"
python3 main.py
```

## Reto 1

- Los datos del CCV se extraen y se pasan a un formato de diccionario, en el módulo [read_csv.py](./read_csv.py).

```python
{
    'Rank': 28,
    'CCA3': 'COL' ,
    'Country': 'Colombia' ,
    'Capital': 'Bogota',
    'Continent': 'South America'
    '2022 Population': 3000,
    '2020 Population': 400,
    '2015 Population': 500,
    'World Population Percentage': 0.12
}
```

---

- Para hacer una gráfica del crecimiento poblacional a través de los años se debe obtener solo los años con su valor correspondiente como entero.

```python
{
    '2022': 3000,
    '2020': 400,
    '2015': 500,
    '2010': 12,
    '2000': 12,
    '1990': 23,
    '1980': 12,
    '1970': 12
}
```

Una solucion es hacer una función que extraiga unicamente los datos de crecimiento poblacional y les de el formato deseado.

```python
def extract_anual_population(data):
    datos_poblacionales = []
    # recorre los datos de cada país
    for country in data:
        # Hace un diccionario tomando unicamente los datos de poblacion anual
        # Formatea para solo tomar el año y pasa la poblacion a entero
        population = {year[0:4]:int(amount) for (year, amount) in country.items() if str(year).endswith('Population')}
        datos_poblacionales.append(population)
    return datos_poblacionales
```

> 📝 **Nota:** Esta funcion se implemento en [read_csv.py](utils.py)

Otra solución es recibiendo unicamente la información de un país, y a partir de ese extraer unicamento los datos de crecimiento poblacional de forma "manual".

```python
def get_population(country_dict):
    # Seleccion manual
    population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values
```

> 📝 **Nota:** Esta adición se hizo en [utils.py](./utils.py)

La primera opcion reacondicionada a funcionar como la segunda opcion.

```python
def get_anual_population(country_dict):
    return {year[0:4]:int(amount) for (year, amount) in country_dict.items() if str(year).endswith('Population')}
```

## Reto 2: Graficando población mundial

Selecciona datos de una columna específica y graficarlos en una gráfica de pastel. Se selecciona la columna *`World Population Percentage`*.

Se propone la siguiente solución dentro del módulo [`utils.py`](utils.py)

```python
def get_world_population_percentage(data):
    # Paises
    labels = [country['Country'] for country in data]
    # Porcentajes de poblacion mundial
    values = [float(country['World Population Percentage']) for country in data]
    return labels, values
```

Se extraen los países y los porcentajes para depués poder pasarlo a la función `generate_pi_chart()` del módulo [`charts.py`](charts.py)

---

La solución dada en clase consiste en el siguiente código

```python
# Reto 2 (Solución de clase)
def yourRun():
    # Se leen datos
    data = read_csv.read_csv('./data.csv')
    # Trae el nombre del país
    countries = list(map(lambda country: country['Country'], data))
    # Trae los porcentajes de población mundial
    percentages = list(map(lambda percentage: percentage['World Population Percentage'], data))
    charts.generate_bar_chart(countries, percentages)
```

Se seleccionan las columnas usando [maps](./../../03%20Funciones/Map.md) usando una lambda function, y luego se hace un parseo a listas.

Para mejorar la visualización de los datos se puede reducir los países por contienente.

```python
data = list(filter(lambda country : country['Continent'] == 'South America', data))
```

## Reto 3: Adaptaciones

Se readapta el proyecto. Para que se genere la grafica de pastel con porcentajes poblacionales de Sudamerica, y que además el usuario ingrese el nombre de un país para usar el

### `main.py`

Se cambia la función `run()`, y se elimina la implementación de los retos 1 y 2.

### `charts.py`

En vez de poner desplegar una ventana con la gráfica, se genera una imagen dentro de la carpeta [imgs](./imgs/) para guardar las gráficas de cada país.

Funciones modificadas:

- `generate_bar_chart`
- `generate_pie_chart`

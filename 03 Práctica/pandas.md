# Pandas

[◀️](./../README.md)

Es una de las líbrerias más usadas de Python. Sirve para analizar y manipular datos de archivos planos como `.csv`.

## Instalación

```sh
pip install pandas
```

## Ejemplo de uso

Al proyecto [**app**](./06-app/), que anteriormente trabajaba con los datos del csv [`data.csv`](./06-app/data.csv) usando los módulos [`read_csv.py`](./06-app/read_csv.py) [`utils.py`](./06-app/utils.py), ahora maneja archivos y datos con pandas.

El primer cambio, se hace a [`main.py`](./06-app/main.py), se importa la libreria de pandas con el alias **pd**.

```python
import pandas as pd
```

Ahora, pandas se encargará de hacer funciones como: leer csv, filtrar columnas, filtrar datos, etc. De tal forma que se tiene el código legado:

```python
# Filtrado por contienente (Se extrae solo Sudamerica)
data = list(filter(lambda country : country['Continent'] == 'South America', data))
# Trae el nombre del país
countries = list(map(lambda country: country['Country'], data))
# Trae los porcentajes de población mundial
percentages = list(map(lambda percentage: percentage['World Population Percentage'], data))
charts.generate_pie_chart(countries, percentages)
```

Y se cambia por el uso de pandas:

```python
# Usando pandas
df = pd.read_csv('data.csv') # dataframe que contiene la información del archivo
# Filtrado por contienente (Se extrae solo Africa)
df = df[df['Continent'] == 'Africa']
# trae países
countries = df['Country'].values
# trae porcentajes
percentages = df['World Population Percentage'].values
charts.generate_pie_chart(countries, percentages)
```

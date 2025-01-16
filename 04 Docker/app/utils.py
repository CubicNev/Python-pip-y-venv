"""
Utilidades para manejar datos poblacionales obtenidos de data.csv
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Fri 20-Dec-2024

Se tienen funcionalidades para tratamiento de datos
"""
# Para enviar datos de crecimiento poblacional a gráfica de barras
# Entrada: País seleccionado en forma de diccionario
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

# Solucion propia
def extract_all_anual_population(data):
    datos_poblacionales = []
    # recorre los datos de cada país
    for country in data:
        # Hace un diccionario tomando unicamente los datos de poblacion anual
        # Formatea para solo tomar el año y pasa la poblacion a entero
        population = {year[0:4]:int(amount) for (year, amount) in country.items() if str(year).endswith('Population')}
        datos_poblacionales.append(population)
    return datos_poblacionales

def get_anual_population(country_dict): return {year[0:4]:int(amount) for (year, amount) in country_dict.items() if str(year).endswith('Population')}

# Obtener la información de un país en especifico, dada una lista de países (lista de diccionarios)
def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result

# Solución propia a Reto 2
def get_world_population_percentage(data):
    # Paises
    labels = [country['Country'] for country in data]
    # Porcentajes de poblacion mundial
    values = [float(country['World Population Percentage']) for country in data]
    return labels, values

"""
Archivo principal para graficar crecimiento poblacional de un país
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Mon 30-Dec-24

Se extrae información de data.csv y se trata la información para graficarla
"""
import utils
import read_csv
import charts
import pandas as pd


def run():
    """ LEGACY
    # Filtrado por contienente (Se extrae solo Sudamerica)
    data = list(filter(lambda country : country['Continent'] == 'South America', data))
    # Trae el nombre del país
    countries = list(map(lambda country: country['Country'], data))
    # Trae los porcentajes de población mundial
    percentages = list(map(lambda percentage: percentage['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    """

    # Usando pandas
    df = pd.read_csv('data.csv') # dataframe que contiene la información del archivo
    # Filtrado por contienente (Se extrae solo Africa)
    df = df[df['Continent'] == 'Africa']
    # trae países
    countries = df['Country'].values
    # trae porcentajes
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)

    # Se leen datos y se obtienen en forma de diccionario
    data = read_csv.read_csv('./data.csv')
    # Ingresa país
    country = input(" Type Country: ")

    # Se selecciona la información del país (trae el diccionario)
    result = utils.population_by_country(data, country)

    # Valida que se haya encontrado un resultado
    if len(result) > 0:
        country_res = result[0]
        # Extrae la infomación que necesitamos
        labels, values = utils.get_population(country_res)
        # Grafica información
        charts.generate_bar_chart(country_res['Country'], labels, values)


if __name__ == '__main__':
    # Nota se hicieron varias funciones ya que plt.show() detiene el programa
    run()
"""
Lector de CSV
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Fri 20-Dec-2024

Módulo encargado de extraer infromación del archivo CSV "data.csv"
"""

import csv

# Función para leer el archivo
def read_csv(path):
    # Se abre con modo lectura
    with open(path, 'r', encoding='UTF-8') as csvfile:
        # Lector recibe el archivo y el tipo de delimitador que usa
        reader = csv.reader(csvfile, delimiter=',')
        # Se extraen los encabezados
        header = next(reader)
        # Lista para guardar los diccionarios generados
        data = []
        # Iteración que lee fila por fila
        for row in reader:
            # Union de encabezado con fila en una lista de tuplas: (columna, valor)
            iterable = zip(header, row)
            # Se pasa a diccionario
            country_dict = {key: value for key, value in iterable}
            # Se agrega el diccionario a la lista
            data.append(country_dict)
        return data

# Correr el archivo como script
if __name__ == '__main__':
    data = read_csv('./data.csv')
    #poblacion_anual = extract_anual_population(data)
    print(data[0])
    #print(poblacion_anual[0])

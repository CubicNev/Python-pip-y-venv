"""
Charts
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Fri 20-Dec-2024

Módulo para hacer gráficas
"""

import matplotlib.pyplot as plt

# Función para hacer una gráfica de pastel con etiquetas
def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    # Obtenemos la figura y las coordenadas
    fig, ax = plt.subplots()
    # Se configura la gráfica
    ax.pie(values, labels=labels)
    # Se genera una imagen
    plt.savefig('pie.png')
    plt.close()
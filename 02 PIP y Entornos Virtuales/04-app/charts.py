"""
Charts
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Fri 20-Dec-2024

Módulo encargado de generar gráficas.
"""
# Importación con alias
import matplotlib.pyplot as plt

# Función para generar gráfica de barras
def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')

# Función para generar grafica de pastel
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    # Lo grafica de forma circular
    ax.axis('equal')
    plt.savefig('pie.png')

# Ejecución del módulo como script
if __name__ == "__main__":
    # Ejemplo
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels,values)

"""
Proyecto: Piedra, papel o tijeras
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 8-Mayo-2024

Programa que simula el juego piedra, papel o tijera. Usa una modalidad de computadora vs jugador.
"""
# Importaciones
import random

# Opciones:
options = ('piedra', 'papel', 'tijera')
rounds = 1

computer_wins = 0
user_wins = 0

while True:

    print('*' * 20)
    print('ROUND', rounds)
    print('*' * 20)

    print('computer_wins:', computer_wins)
    print('user_wins:', user_wins)

    # Se lee la opción del usuario y se pasa a mnusculas
    user_option = input("piedra, papel o tijera: ").lower()

    # Valida que la opcion ingresada se encuentre dentro de las opciones
    if not user_option in options:
        print('Esa opciones no es valida')
        continue

    # Se escoge una opcion de forma aleatoria
    computer_option = random.choice(options)

    #Generan opciones para la computadora
    print('User option:', user_option)
    print('Computer option:', computer_option)

    if user_option == computer_option:
        print("Empate!")
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print("user gano ronda!")
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('computer gana ronda!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra ronda!')
            print("user gano!")
            user_wins += 1
        else:
            print('tijera gana a papel')
            print("computer gano ronda!")
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print("user gano ronda!")
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print("computer gano ronda!")
            computer_wins += 1
    else:
        print("Opcion invalida: ", user_option)

    if computer_wins == 2:
        print(' COMPUTER WINS!!!!')
        break
    elif user_wins == 2:
        print(' USER WINS!!!!')
        break

    rounds += 1
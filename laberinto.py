# laberinto.py
import random

def generar_laberinto(filas, columnas, densidad_paredes):
    laberinto = []

    # Crear un laberinto vacío
    for _ in range(filas):
        fila = [" " for _ in range(columnas)]
        laberinto.append(fila)

    # Añadir paredes aleatoriamente
    for fila in range(1, filas - 1):
        for columna in range(1, columnas - 1):
            if random.random() < densidad_paredes:
                laberinto[fila][columna] = "#"

    # Establecer posición de inicio (S) y meta (E)
    laberinto[0][1] = "S"
    laberinto[filas - 1][columnas - 2] = "E"

    return laberinto

def cargar_niveles(filename):
    with open(filename, "r") as file:
        niveles = [level.strip().split("\n") for level in file.read().strip().split("\n\n")]
    return niveles

# Puedes agregar otras funciones relacionadas con el laberinto y el juego aquí

# Ejemplo de función para verificar si un nivel está completo
def nivel_completo(nivel, player_x, player_y):
    return nivel[player_y][player_x] == "E"

# Ejemplo de función para cargar el siguiente nivel
def cargar_siguiente_nivel(niveles, nivel_actual):
    if nivel_actual < len(niveles) - 1:
        return niveles[nivel_actual + 1]
    else:
        return None

# laberinto.py

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

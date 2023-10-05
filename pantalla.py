# pantalla.py
import pygame

# Colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

def dibujar_laberinto(screen, niveles, nivel_actual, player_x, player_y, CELL_SIZE):
    # Código para dibujar el laberinto en la pantalla
    for y, row in enumerate(niveles[nivel_actual]):
        for x, cell in enumerate(row):
            if cell == "#":
                pygame.draw.rect(screen, YELLOW, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == "E":
                pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, (player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Puedes agregar otras funciones relacionadas con la pantalla e interfaz de usuario aquí

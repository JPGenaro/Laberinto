import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Laberinto")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Representación del laberinto
laberinto = [
    "###########",
    "#S        #",
    "# ### # ## #",
    "#   # #  # #",
    "### # ### # #",
    "#   #      #",
    "#########E#"
]

# Tamaño de celda
CELL_SIZE = WIDTH // len(laberinto[0])

# Posición inicial del jugador
player_x, player_y = 1, 1

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Mover al jugador en función de la tecla presionada
            if event.key == pygame.K_UP and laberinto[player_y - 1][player_x] != "#":
                player_y -= 1
            elif event.key == pygame.K_DOWN and laberinto[player_y + 1][player_x] != "#":
                player_y += 1
            elif event.key == pygame.K_LEFT and laberinto[player_y][player_x - 1] != "#":
                player_x -= 1
            elif event.key == pygame.K_RIGHT and laberinto[player_y][player_x + 1] != "#":
                player_x += 1

    # Verificar si el jugador ha llegado a la salida
    if laberinto[player_y][player_x] == "E":
        print("¡Has ganado!")
        running = False

    # Dibujar el laberinto y al jugador
    screen.fill(WHITE)
    for y, row in enumerate(laberinto):
        for x, cell in enumerate(row):
            if cell == "#":
                pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, (player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

# Finalizar Pygame
pygame.quit()
sys.exit()

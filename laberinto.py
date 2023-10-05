import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Laberinto")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Representación de niveles del laberinto
niveles = [
    [
        "##########################################################",
        "#S        #                 #         #                 #E#",
        "# # ##### # # ##### ##### # # ##### # ##### ##### # ### #",
        "# #   #   #   #   #     #   #   #   #     #   #     #   #",
        "# ### # ### # # # # ### # ##### # ##### ##### ###########",
        "#   #     #   #   #   #   #   #     #   #   # #     #   #",
        "# # ##### ########### # ##### ##### # ##### # ##### # # #",
        "# #     # #   #     # # #   #   #   # #     #   #   # # #",
        "### ### # ##### # ### # ### ### ### ### ### # ##### # # #",
        "#   #   #     # #   # #   #   #   # #     # # #     #   #",
        "# ##### # ### # ##### ### # ##### # ##### ### # #########",
        "#   #   # #   # #   #   #   #     #   #   #     # #     #",
        "# ### ### # ##### # ##### ######### # # # # ##### ##### #",
        "# #   #   #     #   #   #     #   #   #   # #   #     # #",
        "# # ######### # ### # ##### # # ##### ### ### ####### # #",
        "# #   #     # #   # #     # # #   #   #   # #       # # #",
        "# ### # ### ##### # ##### # ##### # # ### ######### # # #",
        "#   # # #   #   #   #     #   #   # #   # #   #     # # #",
        "# ### # # ######### ##### ##### # ##### # # ### ##### # #",
        "#   # #   #   #       #     #   #   #   # #   #       # #",
        "### ##### ### # ##### # ##### ### ### # # ### ###########",
        "#   #   #   # #   #   #   #     #     # #   #           #",
        "# # ### # ##### # ### # ### ##### ##### ######### ##### #",
        "# #   # #     # # #   # # #   #     #   #         #   # #",
        "### # ######### # ##### # ##### ##### ########### # # # #",
        "#   # #   #   #     #   #   #   #   #     #     #   #   #",
        "# ##### # # # ##### ##### # ### # ### ##### # ##### ###",
        "#       #   #             #     #             #           #",
        "##########################################################",
    ],
    [
        "##########################################################",
        "#S               #         #                             #E#",
        "# ######### ##### ##### ##### ##### ##### ##### ##### ### #",
        "# #       #   #   #   #     #     #   #   #   #   #   #   #",
        "# # ##### # # # # # ##### ##### ##### # ##### ##### ##### #",
        "#   #   # #   # # # #   #   #   #   #     #   #   #   #   #",
        "### ### # ##### # # # ### # # # # # ##### # ##### ##### ###",
        "#   #   #   #     #   #   # # # #   #   #     #       #   #",
        "# # ##### # ##### ##### ##### ##### # # ######### ##### # #",
        "# #     # #     #   #   #     #     # #     #     #   #   #",
        "# ##### # # ### # ### # ##### ##### # # ##### # ### ##### #",
        "#   #   #   #   #   # # #   #   #   #   #     #   #   #   #",
        "# ### ##### ##### ### # # # # ##### ##### ##### ##### ### #",
        "#   #   #     #     #   # # #       #   #   #   #   #   # #",
        "# ##### # # ##### ##### # # # ##### # ### ##### # ##### # #",
        "#     #   #       #     # # #     #   #   #     #   #   # #",
        "##### ############# ##### # ##### ##### ########### ### # #",
        "#   #   #         #     # #     #   #     #       #   #   #",
        "# # # ##### # # ##### ### ##### # ######### ### # ##### # #",
        "# #     #   # #   #   #     #   # #     #     #   #   #   #",
        "### ##### ##### ### ##### ##### ### ##### ##### ### # ###",
        "#   #     #   # #     #       #     #         #     #   #",
        "# ##### ##### # ### ##### ######### ##### ##### ##### ### #",
        "#     #       #       #     #     #   #   #       #   #   #",
        "##### ######### ######### ##### ##### ##### ######### ### #",
        "#   # #   #           #       #   #   #     #   #   #   # #",
        "# # # # # # # ##### # ##### # # # ### ##### # ##### ##### #",
        "# #   #   #     #   #   #   #   #   #   #   #   #   #   # #",
        "##########################################################",
    ],
    [
        "##########################################################",
        "#S                 #     #     #     #     #     #       #E#",
        "# ############### ### ### ### ### ### ### ### ### ##### ### #",
        "# #             #   #   #   #   #   #   #   #   #     #   #   #",
        "# ############# ### ### ### ### ### ### ### ######### ##### #",
        "# #           #   #   #   #   #   #   #   #         #   #   #",
        "# ######### ### ### ### ### ### ### ### ######### ### ### ###",
        "#       #   #   #   #   #   #   #   #   #   #   #     #     #",
        "##### ### ### ### ######### ### ### ### ### ### ########### #",
        "#   #     #   #   #   #     #   #   #   #   #   #         # #",
        "# ######### ### ##### ### ######### ### ### ### ######### # #",
        "# #           #   #   #   #   #   #   #   #   # #   #   # # #",
        "# ######### ### ######### ### ### ### ### ### # ### ### # # #",
        "#       #   #     #   #     #   #   #   #   #   # #   #   # #",
        "# ######### ### ### ### ######### ### ### ### ### ##### ### #",
        "#   #     #   #   #   #   #   #   #   #   #   #     #     #",
        "# ### ######### ### ### ### ### ### ### ### ########### ###",
        "#   #       #   #   #   #   #   #   #   #   #         #   #",
        "# ##### ### ### ### ### ### ### ### ### ######### ##### # #",
        "#     #   #   #   #   #   #   #   #   #       #   #   #   #",
        "# ### ### ### ### ### ######### ### ######### ### # ##### #",
        "# #   #   #   #   #     #   #   # #         #   #   #     #",
        "# # ### ### ### ### ##### # ### # # ######### ########### #",
        "# #     #   #   #     #   #   #   #       #   #           #",
        "# ##### ### # ##### # ########### ##### ### ### ######### #",
        "#     #   # #       #         #       #   #   #   #     # #",
        "### ##### # ##### ######### ######### ### ### ### ##### # #",
        "#   #     #     #     #   #         #   #   #   #   #   # #",
        "# ######### ##### ##### ### ######### ##### ##### ### ### #",
        "#                 #     #               #               #   #",
        "##########################################################",
    ],
]

# Tamaño de celda
CELL_SIZE = WIDTH // len(niveles[0][0])

# Nivel actual
nivel_actual = 0

# Posición inicial del jugador
player_x, player_y = 1, 1

# Mensaje de nivel actual
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            try:
                # Mover al jugador en función de la tecla presionada
                if event.key == pygame.K_UP and niveles[nivel_actual][player_y - 1][player_x] != "#":
                    player_y -= 1
                elif event.key == pygame.K_DOWN and niveles[nivel_actual][player_y + 1][player_x] != "#":
                    player_y += 1
                elif event.key == pygame.K_LEFT and niveles[nivel_actual][player_y][player_x - 1] != "#":
                    player_x -= 1
                elif event.key == pygame.K_RIGHT and niveles[nivel_actual][player_y][player_x + 1] != "#":
                    player_x += 1

                # Verificar si el jugador ha llegado a la salida
                if niveles[nivel_actual][player_y][player_x] == "E":
                    nivel_actual += 1
                    if nivel_actual < len(niveles):
                        # Reiniciar la posición del jugador para el próximo nivel
                        player_x, player_y = 1, 1
                    else:
                        print("¡Has completado todos los niveles!")
                        running = False
            except IndexError:
                pass  # Ignora intentos de moverse fuera de los límites del laberinto

    # Dibujar el laberinto y al jugador
    screen.fill(WHITE)
    for y, row in enumerate(niveles[nivel_actual]):
        for x, cell in enumerate(row):
            if cell == "#":
                pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, (player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Mostrar el número de nivel actual en pantalla
    nivel_texto = font.render(f"Nivel {nivel_actual + 1}", True, BLACK)
    screen.blit(nivel_texto, (10, 10))

    pygame.display.update()

# Finalizar Pygame
pygame.quit()
sys.exit()

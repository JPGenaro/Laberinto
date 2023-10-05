# main.py
import pygame
import sys
from laberinto import cargar_niveles
from pantalla import dibujar_laberinto, BLACK, WHITE, GREEN, RED, YELLOW

# Inicializa Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Laberinto - Rintobel")

# Tamaño de celda
CELL_SIZE = min(WIDTH // len(niveles[0][0]), HEIGHT // len(niveles[0]))

# Nivel actual
nivel_actual = 0

# Estado del juego (0: Pantalla de inicio, 1: Jugando, 2: Juego completo)
estado_juego = 0

# Posición inicial del jugador
player_x, player_y = 1, 1

# Mensaje de nivel actual
font = pygame.font.Font(None, 36)

# Mensaje de inicio del juego
inicio_font = pygame.font.Font(None, 48)
inicio_texto = inicio_font.render("Presiona la Barra Espaciadora para Empezar", True, WHITE)
inicio_rect = inicio_texto.get_rect(center=(WIDTH // 2, HEIGHT * 0.8))

# Mensaje del nombre del juego
nombre_juego_font = pygame.font.Font(None, 72)
nombre_juego_texto = nombre_juego_font.render("Rintobel", True, GREEN)
nombre_juego_rect = nombre_juego_texto.get_rect(center=(WIDTH // 2, HEIGHT * 0.4))

# Cargar niveles desde el archivo
niveles = cargar_niveles("niveles.txt")

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if estado_juego == 0:  # Pantalla de inicio
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    estado_juego = 1  # Comenzar el juego

        elif estado_juego == 1:  # Jugando
            if event.type == pygame.KEYDOWN:
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
                            estado_juego = 2  # Juego completo
                except IndexError:
                    pass  # Ignora intentos de moverse fuera de los límites del laberinto

    # Dibujar el fondo negro
    screen.fill(BLACK)

    # Dibujar el laberinto y al jugador
    if estado_juego == 1:
        dibujar_laberinto(screen, niveles, nivel_actual, player_x, player_y, CELL_SIZE)

    # Mostrar el número de nivel actual en pantalla
    if estado_juego == 1:
        nivel_texto = font.render(f"Nivel {nivel_actual + 1}", True, WHITE)
        screen.blit(nivel_texto, (10, 10))
    elif estado_juego == 0:  # Pantalla de inicio
        screen.blit(nombre_juego_texto, nombre_juego_rect)
        screen.blit(inicio_texto, inicio_rect)

    pygame.display.update()

# Finalizar Pygame
pygame.quit()
sys.exit()

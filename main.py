# main.py
import pygame
import sys
from laberinto import cargar_niveles, generar_laberinto
from pantalla import dibujar_laberinto, BLACK, WHITE, GREEN, RED, YELLOW

# Inicializa Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Laberinto - Rintobel")

# Generar un laberinto aleatorio (por ejemplo, 10 filas x 10 columnas con densidad 0.3)
laberinto_aleatorio = generar_laberinto(20, 20, 0.3)

# Tamaño de celda
CELL_SIZE = min(WIDTH // len(laberinto_aleatorio[0]), HEIGHT // len(laberinto_aleatorio)) // 2

# Cargar niveles desde el archivo
niveles = cargar_niveles("niveles.txt")
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
    # Calcular la posición de inicio para dibujar el laberinto
        laberinto_x = (WIDTH - len(niveles[nivel_actual][0]) * CELL_SIZE) // 2
        laberinto_y = (HEIGHT - len(niveles[nivel_actual]) * CELL_SIZE) // 2

        for y, row in enumerate(niveles[nivel_actual]):
            for x, cell in enumerate(row):
                if cell == "#":
                    pygame.draw.rect(screen, YELLOW, (laberinto_x + x * CELL_SIZE, laberinto_y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif cell == "E":
                    pygame.draw.rect(screen, RED, (laberinto_x + x * CELL_SIZE, laberinto_y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, GREEN, (laberinto_x + player_x * CELL_SIZE, laberinto_y + player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Mostrar el número de nivel actual en pantalla
    if estado_juego == 1:
        nivel_texto = font.render(f"Nivel {nivel_actual + 1}", True, WHITE)
        nivel_rect = nivel_texto.get_rect(center=(WIDTH // 2, 30))  # Centrar el texto en la parte superior de la pantalla
        screen.blit(nivel_texto, nivel_rect) 
    elif estado_juego == 0:  # Pantalla de inicio
        screen.blit(nombre_juego_texto, nombre_juego_rect)
        screen.blit(inicio_texto, inicio_rect)

    pygame.display.update()

# Finalizar Pygame
pygame.quit()
sys.exit()

# juego_con_group.py
import pygame
from pygame.sprite import Sprite, Group

# Inicialización de Pygame
pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Ejemplo con Group")
clock = pygame.time.Clock()

# Definición de un sprite personalizado (Jugador)
class Jugador(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))  # Color azul
        self.rect = self.image.get_rect()
        self.rect.center = (200, 150)
    
    def update(self):
        # Movimiento con teclas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Definición de un sprite para "Obstáculo" (enemigos o bloques)
class Obstaculo(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Color rojo
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Crear una instancia del jugador
jugador = Jugador()

# Crear un grupo de sprites para los obstáculos
obstaculos = Group()

# Crear varios obstáculos y añadirlos al grupo
obstaculos.add(Obstaculo(100, 100))
obstaculos.add(Obstaculo(300, 200))
obstaculos.add(Obstaculo(150, 250))

# Crear un grupo general de sprites (jugador + obstáculos)
todos_los_sprites = Group()
todos_los_sprites.add(jugador)
todos_los_sprites.add(obstaculos)

# Bucle principal del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Actualizar todos los sprites (jugador y obstáculos)
    todos_los_sprites.update()

    # Comprobar colisiones entre el jugador y los obstáculos
    if pygame.sprite.spritecollide(jugador, obstaculos, False):
        print("¡Colisión detectada!")

    # Dibujar todos los sprites en la pantalla
    pantalla.fill((30, 30, 30))  # Fondo oscuro
    todos_los_sprites.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Salir de Pygame
pygame.quit()

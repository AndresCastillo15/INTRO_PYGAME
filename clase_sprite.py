# juego_sprite.py
import pygame
from pygame.sprite import Sprite, Group

# Inicialización de Pygame
pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Ejemplo con Sprite y Group")
clock = pygame.time.Clock()

# Definición de un sprite personalizado
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

# Crear una instancia del sprite
jugador = Jugador()

# Crear un grupo de sprites y añadir el jugador
todos_los_sprites = Group()
todos_los_sprites.add(jugador)

# Bucle principal del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Actualizar todos los sprites
    todos_los_sprites.update()

    # Dibujar todos los sprites
    pantalla.fill((30, 30, 30))  # Color de fondo
    todos_los_sprites.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Salir de Pygame
pygame.quit()

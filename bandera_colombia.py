# Importamos la librería pygame
import pygame
import random

# Colores aleatorios
amarillo = (255, 250, 0)
azul = (0, 0, 255)
rojo = (255, 0, 0)

# Inicializamos los módulos de pygame
pygame.init()

# Establecer título a la ventana
pygame.display.set_caption("bandera de colombia")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400, 400))

# Creamos una superficie con el tamaño adecuado (por ejemplo, 300x300)
color_amarillo = pygame.Surface((400, 200))
color_azul = pygame.Surface((400, 100))
color_rojo = pygame.Surface((400, 100))

# Rellenamos la superficie con el color aleatorio
color_amarillo.fill((amarillo))
color_azul.fill((azul))
color_rojo.fill((rojo))

# Insertamos o movemos la superficie en la ventana

ventana.blit(color_amarillo, (0, 0))
ventana.blit(color_azul, (0, 200))
ventana.blit(color_rojo, (0, 300))

# Actualizamos la visualización de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()

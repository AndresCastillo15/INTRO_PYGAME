# Importamos la librería pygame
import pygame
import random

# Colores aleatorios
rojo = random.randint(0, 255)
verde = random.randint(0, 255)
azul = random.randint(0, 255)

# codigo RGB
print("El numero de rojo es:", rojo)
print("El numero de verde es:", verde)
print("El numero de azul es:", azul)

# Inicializamos los módulos de pygame
pygame.init()

# Establecer título a la ventana
pygame.display.set_caption("Surface")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400, 400))

# Creamos una superficie con el tamaño adecuado (por ejemplo, 300x300)
color_aleatorio = pygame.Surface((200, 200))

# Rellenamos la superficie con el color aleatorio
color_aleatorio.fill((rojo, verde, azul))

# Insertamos o movemos la superficie en la ventana
ventana.blit(color_aleatorio, (100, 100))

# Actualizamos la visualización de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()

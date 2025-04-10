import pygame
import sys

rojo = (255, 0, 0)
azul = (0, 0, 255)
amarillo = (255, 250, 0)
morado = (250, 0, 250)
verde = (0, 255, 0)
blanco = (0,0,0)

pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Los cuadrados que rebotan")
clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3
YY = 300
MOVIMIENTOY = 3

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    XX = XX + MOVIMIENTO
    if XX >= 450:
        XX = 450
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3

    YY = YY + MOVIMIENTOY
    if YY >= 450:
        YY = 450
        MOVIMIENTOY = -3
    elif YY <= 0:
        YY = 0
        MOVIMIENTOY = 3

    pygame.draw.rect(ventana, rojo, (XX, 1, 50, 50))
    pygame.draw.rect(ventana, verde, (XX, 450, 50, 50))
    pygame.draw.rect(ventana, morado, (1, YY, 50, 50))
    pygame.draw.rect(ventana, amarillo,(450, YY, 50, 50))
    pygame.draw.rect(ventana, amarillo,(450, YY, 50, 50))
    pygame.draw.rect(ventana, blanco,(200,200,100,100))
    pygame.display.flip()


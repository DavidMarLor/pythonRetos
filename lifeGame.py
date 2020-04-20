import pygame
import numpy as np
import time

pygame.init() #iniciamos la libreria

width, height = 1000,1000 #le damos alto y ancho al escenario
screen = pygame.display.set_mode((height, width))

bg = 25,25,25 #damos color al fondo
screen.fill(bg)

nxC, nyC = 25, 25 #numero de celdas de cada eje

dimCW = width / nxC #ancho y alto de cada celda
dimCH = height / nyC 

#Estado de las celdas vivas = 1 y muertas = 0
gameState = np.zeros((nxC, nyC))

#bucle para ejecucion infinita.
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)#Para evitar que se superponga
    time.sleep(0.1)

    for y in range(0, nxC):
        for x in range(0, nyC):
            #Calculamos el numero de vecinos cercanos
            n_neigh = gameState[(x-1) % nxC, (y-1)% nyC] + \
                      gameState[(x)  % nxC, (y-1) % nyC] + \
                      gameState[(x+1) % nxC, (y-1) % nyC] + \
                      gameState[(x-1) % nxC, (y)  % nyC] + \
                      gameState[(x+1) % nxC, (y)  % nyC] + \
                      gameState[(x-1) % nxC, (y+1) % nyC] + \
                      gameState[(x)  % nxC, (y+1) % nyC] + \
                      gameState[(x+1) % nxC, (y+1) % nyC]

            #Reglas
            #1. Una celula muerta con exactamente 3 vecinas vias, "revive"
            if gameState[x,y] == 0 and n_neigh == 3:
                newGameState[x,y] = 1

            #2. Una celula viva con menos de 2 o mas vecinas vivas, "muere"
            #elif gameState == 1 and (n_neigh < 2 or n_neigh > 3):
            #    newGameState[x,y] = 0

            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly)#dibujar los poligonos de la vida.
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly)#en caso de vida pintar de blanco

    #Actualizamos el estado del juego.
    gameState = np.copy(newGameState)

    #Actualizamos la pantalla.
    pygame.display.flip()

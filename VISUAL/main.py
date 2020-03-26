import pygame
import math
from random import randrange
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

#Is game active?
running = True
#Window Size
width = 700
height = 700
#Color Presets
windowBG = (255, 255, 255)
dendriteColor = (0, 0, 255)
axonColor = (255, 0, 0)
somaColor = (0, 0, 0)
#Position Defining
global somaX
global somaY
somaX = int()
somaY = int()

xMid = int(width/2)
yMid = int(height/2)
#Framerate AKA FPS Controller Definer
clock = pygame.time.Clock()

#Set window size
window = pygame.display.set_mode((width,height))
#Set window BG Color
window.fill(windowBG)

def findSquareArea(x, y, length):
    length = length/3
    xEndpoint = x + length * math.cos(randrange(360))
    yEndpoint = y + length * math.sin(randrange(360))
    return xEndpoint, yEndpoint

dendriteBranchLog = []
def dendriteTreeGeneration(branches):
    initXend = randrange(200, 500)
    initYend = randrange(200, 500)
    dendriteBranchLog.append([initXend, initYend])

    somaDistance = round(
        math.sqrt(
            ((initXend - somaX) ** 2)
            +
            ((initYend - somaY) ** 2)
        )
    )

    pygame.draw.line(
        window,
        dendriteColor,
        (somaX, somaY),
        (
        dendriteBranchLog[0][0],
        dendriteBranchLog[0][1],
        ), 2
    );

    for n in range(branches):
        pygame.draw.line(
            window,
            dendriteColor,
            (dendriteBranchLog[0][0], dendriteBranchLog[0][1]),
            (findSquareArea(
                dendriteBranchLog[0][0],
                dendriteBranchLog[0][1],
                somaDistance)
            ),
            2);

axonBranchLog = []
def axonTreeGeneration(branches):
    initXend = randrange(200, 500)
    initYend = randrange(200, 500)
    pygame.draw.line(
        window,
        axonColor,
        (somaX, somaY),
        (initXend, initYend),
        2);
    axonBranchLog.append([initXend, initYend])
    originalLength = round(
        math.sqrt(
            ((initXend - somaX) ** 2)
            +
            ((initYend - somaY) ** 2)
        )
    )
    for n in range(branches):
        pygame.draw.line(
            window,
            axonColor,
            (axonBranchLog[0][0], axonBranchLog[0][1]),
            (findSquareArea(
                axonBranchLog[0][0],
                axonBranchLog[0][1],
                originalLength)
            ),
            2);

def placeSoma():
    pygame.draw.circle(window, somaColor, (somaX, somaY), 10)

somaX = randrange(200, 500)
somaY = randrange(200, 500)
placeSoma()
dendriteTreeGeneration(randrange(15))
axonTreeGeneration(randrange(15))

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
    clock.tick(60)
    pygame.display.flip()

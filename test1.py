# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Fill the screen with white
screen.fill((255, 255, 255))

# Variable to keep the main loop running
running = True

xPos = 16
yPos = 16

# Main loop
while running:
    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((16, 16))
    screen.blit(surf, (xPos, yPos))

    # Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    for pixel in range(SCREEN_WIDTH):
        if xPos >= SCREEN_WIDTH:
            if yPos >= SCREEN_HEIGHT:
                pass
        elif xPos < SCREEN_WIDTH:
            xPos += 32
            screen.blit(surf, (xPos, yPos))
            if yPos < SCREEN_HEIGHT:
                yPos += 32
                    screen.blit(surf, (xPos, yPos))
        else:
            pass
        pygame.display.flip()

    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

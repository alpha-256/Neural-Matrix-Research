import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((700, 700))
FPSCLOCK = pygame.time.Clock()
RED = pygame.Color("red")
startpoint = pygame.math.Vector2(350, 350)
endpoint = pygame.math.Vector2(300, 0)
angle = 0
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # % 360 to keep the angle between 0 and 360.
    angle = (angle+5) % 360
    # The current endpoint is the startpoint vector + the
    # rotated original endpoint vector.
    current_endpoint = startpoint + endpoint.rotate(angle)

    screen.fill((0, 0, 0))
    pygame.draw.line(screen, RED, startpoint, current_endpoint, 2)

    pygame.display.flip()
    FPSCLOCK.tick(60)

pygame.quit()
sys.exit()

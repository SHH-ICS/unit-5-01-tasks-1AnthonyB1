# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame, sys

pygame.init()
Display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("The Sunrise of Anthony")

Clock = pygame.time.Clock()
FPS = 60

while True:
    Display.fill((100, 70, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Render Stuff Here
    pygame.draw.circle(Display, (255, 200, 0), (250,250), 150)
    pygame.draw.line(Display, (100, 200, 100), (0, 500), (500, 500), 400)
  
    pygame.draw.circle(Display, (255, 255, 255), (100, 75), 30)
    pygame.draw.circle(Display, (255, 255, 255), (60, 80), 30)
    pygame.draw.circle(Display, (255, 255, 255), (140, 80), 30)

    pygame.display.flip()
    Clock.tick(60)

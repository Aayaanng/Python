import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
pygame.display.set_caption("Circle genorator")

class Circle():
    def __init__(self):
        self.x = randint(-50, 500)
        self.y = randint(0, 500)
        self.r = randint(10, 50)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
C1 = Circle()
C2 = Circle()
C3 = Circle()
C4 = Circle()
C5 = Circle()
C6 = Circle()
C7 = Circle()
C8 = Circle()
C9 = Circle()
C10 = Circle()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 255))
    C1.draw()
    C2.draw()
    C3.draw()
    C4.draw()
    C5.draw()
    C6.draw()
    C7.draw()
    C8.draw()
    C9.draw()
    C10.draw()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
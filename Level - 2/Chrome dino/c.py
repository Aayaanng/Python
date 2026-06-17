import pygame
import random 

pygame.init()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chrome dino")
clock = pygame.time.Clock()

running = True

class dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\Users\aayaa\OneDrive\Desktop\Coding\Python\Python\Level - 2\Chrome dino\dino.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 85))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH//7-self.rect.width
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 10
        self.is_jumping = False
        self.jump_speed = 12
    def update(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
        if self.is_jumping:
            self.rect.y -= self.is_jumping
            self.jump_speed = -1

            if self.jump_speed < -12:
                self.is_jumping = False
                self.jump_speed = 12
class cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Python\pygame and oops\Chrome dino\cactus.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,70))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = SCREEN_HEIGHT - self.rect.height -10
    def update(self):
        self.rect.x -= 5
        if self.rect.x < -60:
            self.rect.x = 700
dino_obj = dino()
cactus_obj = cactus()

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    cactus_obj.update()
    dino_obj.update()
    screen.fill((255, 255, 255))
    screen.blit(dino_obj.image, dino_obj.rect)
    screen.blit(cactus_obj.image, cactus_obj.rect)
    pygame.display.update()
pygame.quit()
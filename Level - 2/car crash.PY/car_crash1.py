import pygame
import random

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Playercar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()
        self.speed = 0
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.width // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            

class Enemycar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()
        self.speed = random.randint(1,5)
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-200, -50)
        while True:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            if abs(self.rect.x - player_car.rect.x) > 100:
                break
        self.rect.y = random.randint(-200, -50)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
enemy_cars = pygame.sprite.Group()

player_car = Playercar()
all_sprites.add(player_car)

game_over = False
score = 0
start_ticks = pygame.time.get_ticks()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_car.speed = -5
            elif event.key == pygame.K_RIGHT:
                player_car.speed = 5

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player_car.speed < 0:
                player_car.speed = 0
            elif event.key == pygame.K_RIGHT and player_car.speed > 0:
                player_car.speed = 0

    if random.randint(0, 100) < 2:
        enemy_car = Enemycar()
        all_sprites.add(enemy_car)
        enemy_cars.add(enemy_car)

    all_sprites.update()

    if pygame.time.get_ticks() - start_ticks > 2000:
        if pygame.sprite.spritecollide(player_car, enemy_cars, False): 
            game_over = True

    screen.fill(BLACK)
    all_sprites.draw(screen)

    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])
    score = (pygame.time.get_ticks() - start_ticks) // 1000

    pygame.display.flip()
    clock.tick(60)

font = pygame.font.Font(None, 72)
game_over_text = font.render("Game Over", True, RED)
screen.blit(
    game_over_text,
    [
        SCREEN_WIDTH // 2 - game_over_text.get_width()//2,
        SCREEN_HEIGHT//2 - game_over_text.get_height()//2
    ]
)

pygame.display.flip()
pygame.time.delay(2000)

pygame.quit()
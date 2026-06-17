import pygame
import random
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

ENEMY_SPAWN_RATE = 80  
DIFFICULTY_INCREASE_RATE = 5000  

class Playercar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.create_car_surface(RED)
        self.rect = self.image.get_rect()
        self.speed = 0
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.width // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 10
        self.health = 3
        self.invincible = False
        self.invincible_timer = 0

    def create_car_surface(self, color):
        surf = pygame.Surface((50, 80), pygame.SRCALPHA)
        pygame.draw.rect(surf, color, (10, 20, 30, 50))
        pygame.draw.rect(surf, (100, 100, 200), (15, 15, 20, 30))
        pygame.draw.circle(surf, BLACK, (10, 70), 5)
        pygame.draw.circle(surf, BLACK, (40, 70), 5)
        pygame.draw.circle(surf, BLACK, (10, 25), 5)
        pygame.draw.circle(surf, BLACK, (40, 25), 5)
        return surf

    def update(self):
        self.rect.x += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.invincible_timer > 2000:  
                self.invincible = False

    def hit(self):
        if not self.invincible:
            self.health -= 1
            self.invincible = True
            self.invincible_timer = pygame.time.get_ticks()
            return True
        return False

class Enemycar(pygame.sprite.Sprite):
    def __init__(self, difficulty=1):
        super().__init__()
        self.image = self.create_car_surface((100, 100, 100))
        self.rect = self.image.get_rect()
        self.speed = random.randint(2, 4 + difficulty // 2)
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-200, -50)
        
        player_car = get_player_car()
        if player_car:
            while abs(self.rect.x - player_car.rect.x) < 100:
                self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)

    def create_car_surface(self, color):
        surf = pygame.Surface((50, 80), pygame.SRCALPHA)

        pygame.draw.rect(surf, color, (10, 20, 30, 50))

        pygame.draw.rect(surf, (50, 50, 80), (15, 15, 20, 30))

        pygame.draw.circle(surf, BLACK, (10, 70), 5)
        pygame.draw.circle(surf, BLACK, (40, 70), 5)
        return surf

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, power_type):
        super().__init__()
        self.type = power_type  
        self.image = self.create_powerup_surface()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3

    def create_powerup_surface(self):
        surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        if self.type == 'shield':
            pygame.draw.circle(surf, (0, 255, 255), (15, 15), 12)
            pygame.draw.circle(surf, WHITE, (15, 15), 8)
        elif self.type == 'slow':
            pygame.draw.rect(surf, (0, 255, 0), (5, 5, 20, 20))
            pygame.draw.rect(surf, WHITE, (10, 10, 10, 10))
        elif self.type == 'score':
            pygame.draw.polygon(surf, (255, 255, 0), [(15, 5), (25, 15), (15, 25), (5, 15)])
        return surf

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

def get_player_car():
    for sprite in all_sprites:
        if isinstance(sprite, Playercar):
            return sprite
    return None

def show_text(screen, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def game_over_screen(screen, score):
    screen.fill(BLACK)
    show_text(screen, "GAME OVER", 72, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
    show_text(screen, f"Final Score: {score}", 48, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    show_text(screen, "Press SPACE to play again or ESC to quit", 36, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False
    return False

def main():
    global all_sprites, enemy_cars
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Car crash simulator")
    clock = pygame.time.Clock()
    
    all_sprites = pygame.sprite.Group()
    enemy_cars = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    
    player_car = Playercar()
    all_sprites.add(player_car)
    
    score = 0
    start_ticks = pygame.time.get_ticks()
    difficulty = 1
    last_difficulty_increase = start_ticks
    powerup_spawn_timer = 0
    
    road_lines = []
    for i in range(10):
        road_lines.append({'y': i * 80, 'x': SCREEN_WIDTH // 2 - 5})
    
    running = True
    game_over = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_car.speed = -6
                elif event.key == pygame.K_RIGHT:
                    player_car.speed = 6
                elif event.key == pygame.K_UP:
                    player_car.speed *= 1.5
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    player_car.speed = 0
        
        if not game_over:
            current_time = pygame.time.get_ticks()
            if current_time - last_difficulty_increase > DIFFICULTY_INCREASE_RATE:
                difficulty += 1
                last_difficulty_increase = current_time
                print(f"Difficulty increased to level {difficulty}")
            
            spawn_rate = max(20, ENEMY_SPAWN_RATE - difficulty)
            if random.randint(0, spawn_rate) < 2:
                enemy_car = Enemycar(difficulty)
                all_sprites.add(enemy_car)
                enemy_cars.add(enemy_car)
            
            if random.randint(0, 200) < 1:
                powerup = PowerUp(
                    random.randint(50, SCREEN_WIDTH - 50),
                    -30,
                    random.choice(['shield', 'slow', 'score'])
                )
                all_sprites.add(powerup)
                powerups.add(powerup)
            
            all_sprites.update()
            
            collisions = pygame.sprite.spritecollide(player_car, enemy_cars, True)
            for collision in collisions:
                if player_car.hit():
                    print(f"Hit! Health: {player_car.health}")
                    if player_car.health <= 0:
                        game_over = True
            
            powerup_collisions = pygame.sprite.spritecollide(player_car, powerups, True)
            for powerup in powerup_collisions:
                if powerup.type == 'shield':

                    player_car.invincible = True
                    player_car.invincible_timer = pygame.time.get_ticks()
                    score += 50
                elif powerup.type == 'slow':

                    for enemy in enemy_cars:
                        enemy.speed = max(1, enemy.speed - 2)
                    score += 30
                elif powerup.type == 'score':
                    score += 100

            score = (pygame.time.get_ticks() - start_ticks) // 100
            
            screen.fill(BLACK)
            
            for line in road_lines:
                pygame.draw.rect(screen, WHITE, (line['x'], line['y'], 10, 40))
                line['y'] += 5
                if line['y'] > SCREEN_HEIGHT:
                    line['y'] = -40
            
            pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 5)
            
            all_sprites.draw(screen)
            
            show_text(screen, f"Score: {score}", 36, WHITE, 70, 30)
            show_text(screen, f"Health: {'❤️' * player_car.health}", 36, RED, 150, 80)
            show_text(screen, f"Level: {difficulty}", 36, YELLOW, 130, 130)
            
            if player_car.invincible:
                alpha = (pygame.time.get_ticks() // 100) % 2
                if alpha:
                    show_text(screen, "SHIELD ACTIVE", 24, (0, 255, 255), SCREEN_WIDTH // 2, 50)
        
        else:
            if game_over_screen(screen, score):
                return main()
            else:
                running = False
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
import sys
try:
    import pygame
except ImportError:
    print("Pygame is not installed. Please install it using 'pip install pygame'")
    sys.exit(1)
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = 3
        self.speed_y = 3
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
class BouncingBall(Ball):
    def move(self):
        super().move()
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y *= -1
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ball bouncing animation using inheritance")
    ball_obj = BouncingBall(100, 100, 20, RED)
    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        ball_obj.move()
        ball_obj.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
if __name__ == "__main__":
    main()

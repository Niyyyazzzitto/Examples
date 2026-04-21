import pygame
import sys
import random
from pygame.locals import *

pygame.init()

# НАСТРОЙКИ ИГРЫ
FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game (Zero Dependency)")

# ЦВЕТА
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100) # Цвет асфальта
YELLOW = (255, 255, 0) # Цвет разделительной полосы

font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 40)

enemy_speed = 7
passed_enemies = 0

# КЛАСС ИГРОКА (Синий прямоугольник)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Создаем поверхность вместо картинки
        self.image = pygame.Surface((50, 90))
        self.image.fill(BLUE) 
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# КЛАСС ВРАГА (Красный прямоугольник)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Создаем поверхность вместо картинки
        self.image = pygame.Surface((50, 90))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -60)

    def move(self):
        global passed_enemies
        self.rect.move_ip(0, enemy_speed)

        if self.rect.top > SCREEN_HEIGHT:
            passed_enemies += 1
            self.reset_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
def show_info():
    passed_text = font.render(f"Passed: {passed_enemies}", True, BLACK)
    DISPLAYSURF.blit(passed_text, (10, 10))

def game_over():
    DISPLAYSURF.fill(BLACK)
    game_over_text = big_font.render("GAME OVER", True, RED)
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    DISPLAYSURF.blit(game_over_text, game_over_rect)
    
    pygame.display.update()
    pygame.time.delay(2000) 
    pygame.quit()
    sys.exit()

# СОЗДАЕМ ОБЪЕКТЫ
P1 = Player()
E1 = Enemy()

# ГЛАВНЫЙ ЦИКЛ
line_y = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()

    if P1.rect.colliderect(E1.rect):
        game_over()

    DISPLAYSURF.fill(GRAY)
    
    line_y = (line_y + enemy_speed) % 40
    for i in range(-40, SCREEN_HEIGHT, 40):
        pygame.draw.rect(DISPLAYSURF, YELLOW, (SCREEN_WIDTH//2 - 5, i + line_y, 10, 20))
    # ------------------------------------------

    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    show_info()

    pygame.display.update()
    FramePerSec.tick(FPS)
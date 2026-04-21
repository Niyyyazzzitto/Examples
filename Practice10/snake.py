import pygame
import random
import sys

pygame.init()

CELL = 20
GRID_W = 15
GRID_H = 20
WIDTH = CELL * GRID_W
HEIGHT = CELL * GRID_H

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 18)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
DARK_GREEN = (0, 120, 0)
RED = (220, 0, 0)

# ХАК: Зашитые уровни (никакие txt файлы не нужны!)
LEVELS = {
    1: ["###############", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "#.............#", "###############"],
    2: ["###############", "#.............#", "#...#####.....#", "#.............#", "#.............#", "#.....###.....#", "#.............#", "#.............#", "#...####......#", "#.............#", "#.............#", "#.........#...#", "#.........#...#", "#..#####..#...#", "#.........#...#", "#.............#", "#....###......#", "#.............#", "#.............#", "###############"],
    3: ["###############", "#.......#.....#", "#.......#.....#", "#...#####.....#", "#.............#", "#.............#", "#.............#", "#...#####.....#", "#...#...#.....#", "#...#...#.....#", "#.......#.....#", "#.......#.....#", "#.............#", "#.......#.....#", "#...#####.....#", "#...#.........#", "#...#.........#", "#.............#", "#.............#", "###############"]
}

snake = [(3, 2), (2, 2), (1, 2)]
direction = (1, 0)
next_direction = (1, 0)
score = 0
level = 1
speed = 5
walls = set()
food = None

def load_level(level_num):
    global walls
    walls = set()
    if level_num not in LEVELS:
        return False # Уровни закончились
    for y, line in enumerate(LEVELS[level_num]):
        for x, char in enumerate(line):
            if char == '#': 
                walls.add((x, y))
    return True

def generate_food():
    while True:
        pos = (random.randint(0, GRID_W - 1), random.randint(0, GRID_H - 1))
        if pos not in snake and pos not in walls:
            return pos

def draw_cell(pos, color):
    pygame.draw.rect(screen, color, (pos[0] * CELL, pos[1] * CELL, CELL, CELL))

def draw_background():
    for y in range(GRID_H):
        for x in range(GRID_W):
            color = WHITE if (x + y) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (x * CELL, y * CELL, CELL, CELL))

def draw_game():
    draw_background()
    for w in walls: draw_cell(w, BLACK)
    for i, part in enumerate(snake):
        draw_cell(part, GREEN if i == 0 else DARK_GREEN)
    if food: draw_cell(food, RED)
    
    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, BLACK), (200, 10))
    pygame.display.update()

def game_over():
    screen.fill(WHITE)
    screen.blit(font.render("GAME OVER", True, RED), (WIDTH//2 - 55, HEIGHT//2 - 20))
    screen.blit(font.render(f"Score: {score}", True, BLACK), (WIDTH//2 - 40, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

def next_level():
    global level, speed, food, snake, direction, next_direction
    level += 1
    speed += 2
    if not load_level(level):
        screen.fill(WHITE)
        screen.blit(font.render("YOU WIN!", True, GREEN), (WIDTH//2 - 45, HEIGHT//2))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()
        
    snake = [(3, 2), (2, 2), (1, 2)]
    direction = (1, 0)
    next_direction = (1, 0)
    for part in snake:
        if part in walls: game_over()
    food = generate_food()

load_level(level)
food = generate_food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1): next_direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1): next_direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0): next_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0): next_direction = (1, 0)

    direction = next_direction
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Проверка столкновений
    if new_head in walls or new_head[0] < 0 or new_head[0] >= GRID_W or new_head[1] < 0 or new_head[1] >= GRID_H or new_head in snake:
        game_over()

    snake.insert(0, new_head)

    # Проверка еды
    if new_head == food:
        score += 1
        food = generate_food()
        if score % 3 == 0: # Каждые 3 очка - новый уровень
            next_level()
    else:
        snake.pop()

    draw_game()
    clock.tick(speed)
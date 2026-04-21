import pygame
import datetime
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Загрузка картинок (убедись, что они лежат в папке images)
clock = pygame.image.load("images/clock.png")
left_hand = pygame.image.load("images/left_hand.png").convert()
left_hand.set_colorkey((255, 255, 255))
right_hand = pygame.image.load("images/right_hand.png").convert()
right_hand.set_colorkey((255, 255, 255))

center = (WIDTH//2, HEIGHT//2)

clock_timer = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # Получаем текущее время
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    # Вычисляем угол поворота (1 секунда/минута = 6 градусов)
    # Знак минус нужен, так как в Pygame поворот по умолчанию идет против часовой стрелки
    second_angle = -seconds * 6
    minute_angle = -minutes * 6

    # Вращаем картинки стрелок
    rotated_left = pygame.transform.rotate(left_hand, second_angle)
    rotated_right = pygame.transform.rotate(right_hand, minute_angle)

    # Получаем новые прямоугольники для отцентрированной отрисовки
    left_rect = rotated_left.get_rect(center=center)
    right_rect = rotated_right.get_rect(center=center)

    # Заливаем фон белым цветом
    screen.fill((255, 255, 255))

    # Отрисовываем циферблат по центру
    clock_rect = clock.get_rect(center=center)
    screen.blit(clock, clock_rect)
    
    # Отрисовываем руки-стрелки
    screen.blit(rotated_right, right_rect)
    screen.blit(rotated_left, left_rect)

    pygame.display.update()
    clock_timer.tick(60)

pygame.quit()
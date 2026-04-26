import pygame
import random
from ui import small_font, font, draw_text

# Константы экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, color_name):
        super().__init__()
        self.image = pygame.Surface((40, 80))
        # Применяем цвет из настроек
        colors = {"BLUE": BLUE, "GREEN": GREEN, "WHITE": WHITE}
        self.image.fill(colors.get(color_name, BLUE))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70))
        
        # Статусы бонусов
        self.shield_active = False
        self.nitro_active = False
        self.powerup_timer = 0
        self.powerup_name = ""

    def update(self):
        keys = pygame.key.get_pressed()
        speed = 10 if self.nitro_active else 5
        
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(speed, 0)
            
        # Таймер бонусов
        if self.powerup_timer > 0:
            self.powerup_timer -= 1
            if self.powerup_timer <= 0:
                self.shield_active = False
                self.nitro_active = False
                self.powerup_name = ""

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.shield_active:
            pygame.draw.rect(surface, CYAN, self.rect, 3) # Обводка щита

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed_modifier):
        super().__init__()
        self.image = pygame.Surface((40, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), -100))
        self.speed = random.randint(3, 6) + speed_modifier

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, speed_modifier):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill(BLACK) # Барьер или яма
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), -50))
        self.speed = 3 + speed_modifier

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self, speed_modifier):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), -50))
        self.speed = 3 + speed_modifier
        self.value = random.choice([1, 1, 1, 5]) # Вес монеток: чаще 1, редко 5

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, speed_modifier):
        super().__init__()
        self.type = random.choice(["Nitro", "Shield", "Repair"])
        self.image = pygame.Surface((30, 30))
        if self.type == "Nitro": self.image.fill(YELLOW)
        elif self.type == "Shield": self.image.fill(CYAN)
        else: self.image.fill(GREEN)
        
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), -50))
        self.speed = 3 + speed_modifier

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

def run_game(screen, settings):
    clock = pygame.time.Clock()
    
    # Настройки сложности
    difficulty_mod = {"Easy": 0, "Medium": 2, "Hard": 5}[settings["difficulty"]]
    
    player = Player(settings["color"])
    enemies = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    # Таймеры спавна
    SPAWN_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_ENEMY, max(500, 1500 - difficulty_mod * 150))
    SPAWN_OBSTACLE = pygame.USEREVENT + 2
    pygame.time.set_timer(SPAWN_OBSTACLE, 2000)
    SPAWN_COIN = pygame.USEREVENT + 3
    pygame.time.set_timer(SPAWN_COIN, 1000)
    SPAWN_POWERUP = pygame.USEREVENT + 4
    pygame.time.set_timer(SPAWN_POWERUP, 7000) # Редко

    score = 0
    distance = 0
    health = 1
    line_y = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SPAWN_ENEMY:
                e = Enemy(difficulty_mod + distance // 1000) # Ускорение со временем
                enemies.add(e)
                all_sprites.add(e)
            if event.type == SPAWN_OBSTACLE:
                o = Obstacle(difficulty_mod + distance // 1000)
                obstacles.add(o)
                all_sprites.add(o)
            if event.type == SPAWN_COIN:
                c = Coin(difficulty_mod + distance // 1000)
                coins.add(c)
                all_sprites.add(c)
            if event.type == SPAWN_POWERUP:
                p = PowerUp(difficulty_mod)
                powerups.add(p)
                all_sprites.add(p)

        # Движение дороги
        screen.fill(GRAY)
        road_speed = 10 if player.nitro_active else 5 + difficulty_mod + distance // 1000
        line_y = (line_y + road_speed) % 40
        for i in range(-40, SCREEN_HEIGHT, 40):
            pygame.draw.rect(screen, YELLOW, (SCREEN_WIDTH // 2 - 5, i + line_y, 10, 20))

        # Обновление спрайтов
        player.update()
        for s in all_sprites:
            if s != player: s.update()
            
        # Коллизии
        if pygame.sprite.spritecollideany(player, enemies) or pygame.sprite.spritecollideany(player, obstacles):
            if player.shield_active:
                player.shield_active = False # Щит спасает 1 раз
                player.powerup_name = ""
                player.powerup_timer = 0
                for e in enemies: e.kill() # Очищаем экран, чтобы не умереть сразу снова
                for o in obstacles: o.kill()
            else:
                health -= 1
                if health <= 0:
                    return score, distance # Игра окончена, возвращаем результаты

        # Сбор монет
        collected_coins = pygame.sprite.spritecollide(player, coins, True)
        for c in collected_coins:
            score += c.value

        # Сбор бонусов
        collected_powerups = pygame.sprite.spritecollide(player, powerups, True)
        for p in collected_powerups:
            player.powerup_name = p.type
            if p.type == "Nitro":
                player.nitro_active = True
                player.powerup_timer = 180 # 3 секунды при 60 fps
            elif p.type == "Shield":
                player.shield_active = True
                player.powerup_timer = 300 # 5 секунд
            elif p.type == "Repair":
                health = min(2, health + 1)
                player.powerup_name = "Repaired!"
                player.powerup_timer = 60

        # Отрисовка
        for s in all_sprites:
            s.draw(screen) if hasattr(s, 'draw') else screen.blit(s.image, s.rect)

        distance += road_speed // 5

        # UI во время игры
        draw_text(screen, f"Score: {score}", font, BLACK, (60, 20))
        draw_text(screen, f"Dist: {distance}m", font, BLACK, (SCREEN_WIDTH - 80, 20))
        if player.powerup_name:
            draw_text(screen, f"Active: {player.powerup_name} ({player.powerup_timer//60}s)", small_font, RED, (SCREEN_WIDTH // 2, 20))

        pygame.display.update()
        clock.tick(60)
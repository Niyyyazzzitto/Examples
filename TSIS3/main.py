import pygame
import sys
import persistence
from ui import Button, draw_text, big_font, font
from racer import run_game, SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TSIS 3: Advanced Racer")
clock = pygame.time.Clock()

settings = persistence.load_settings()

def get_player_name():
    """Простой экран для ввода имени перед игрой"""
    name = ""
    while True:
        screen.fill((50, 50, 50))
        draw_text(screen, "ENTER YOUR NAME:", font, (255, 255, 255), (SCREEN_WIDTH // 2, 200))
        draw_text(screen, name + "_", big_font, (255, 255, 0), (SCREEN_WIDTH // 2, 280))
        draw_text(screen, "Press ENTER to start", font, (200, 200, 200), (SCREEN_WIDTH // 2, 400))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name != "":
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 10:
                    name += event.unicode
                    
        pygame.display.update()
        clock.tick(30)

def main_menu():
    btn_play = Button(100, 200, 200, 50, "Play")
    btn_leaderboard = Button(100, 270, 200, 50, "Leaderboard")
    btn_settings = Button(100, 340, 200, 50, "Settings")
    btn_quit = Button(100, 410, 200, 50, "Quit")

    while True:
        screen.fill((200, 200, 200))
        draw_text(screen, "RACER GAME", big_font, (0, 0, 0), (SCREEN_WIDTH // 2, 100))

        for btn in [btn_play, btn_leaderboard, btn_settings, btn_quit]:
            btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                
            if btn_play.is_clicked(event):
                player_name = get_player_name()
                score, distance = run_game(screen, settings)
                persistence.save_score(player_name, score, distance)
                game_over_screen(score, distance)
            
            if btn_leaderboard.is_clicked(event):
                leaderboard_screen()
            
            if btn_settings.is_clicked(event):
                settings_screen()
                
            if btn_quit.is_clicked(event):
                pygame.quit(); sys.exit()

        pygame.display.update()
        clock.tick(60)

def settings_screen():
    global settings
    btn_color = Button(50, 150, 300, 50, f"Car Color: {settings['color']}")
    btn_diff = Button(50, 220, 300, 50, f"Difficulty: {settings['difficulty']}")
    btn_sound = Button(50, 290, 300, 50, f"Sound: {'ON' if settings['sound'] else 'OFF'}")
    btn_back = Button(100, 450, 200, 50, "Back")

    while True:
        screen.fill((200, 200, 200))
        draw_text(screen, "SETTINGS", big_font, (0, 0, 0), (SCREEN_WIDTH // 2, 60))

        for btn in [btn_color, btn_diff, btn_sound, btn_back]:
            btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                
            if btn_color.is_clicked(event):
                colors = ["BLUE", "GREEN", "WHITE"]
                idx = (colors.index(settings['color']) + 1) % 3
                settings['color'] = colors[idx]
                btn_color.text = f"Car Color: {settings['color']}"
                
            if btn_diff.is_clicked(event):
                diffs = ["Easy", "Medium", "Hard"]
                idx = (diffs.index(settings['difficulty']) + 1) % 3
                settings['difficulty'] = diffs[idx]
                btn_diff.text = f"Difficulty: {settings['difficulty']}"
                
            if btn_sound.is_clicked(event):
                settings['sound'] = not settings['sound']
                btn_sound.text = f"Sound: {'ON' if settings['sound'] else 'OFF'}"
                
            if btn_back.is_clicked(event):
                persistence.save_settings(settings)
                return

        pygame.display.update()
        clock.tick(60)

def leaderboard_screen():
    lb = persistence.load_leaderboard()
    btn_back = Button(100, 500, 200, 50, "Back")

    while True:
        screen.fill((200, 200, 200))
        draw_text(screen, "TOP 10 SCORES", big_font, (0, 0, 0), (SCREEN_WIDTH // 2, 50))

        y_offset = 120
        for i, entry in enumerate(lb):
            text = f"{i+1}. {entry['name']} - {entry['score']} pts ({entry['distance']}m)"
            draw_text(screen, text, font, (0, 0, 0), (SCREEN_WIDTH // 2, y_offset))
            y_offset += 35

        btn_back.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if btn_back.is_clicked(event):
                return

        pygame.display.update()
        clock.tick(60)

def game_over_screen(score, distance):
    btn_retry = Button(100, 350, 200, 50, "Retry")
    btn_menu = Button(100, 420, 200, 50, "Main Menu")

    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, "GAME OVER", big_font, (255, 0, 0), (SCREEN_WIDTH // 2, 150))
        draw_text(screen, f"Score: {score}", font, (255, 255, 255), (SCREEN_WIDTH // 2, 230))
        draw_text(screen, f"Distance: {distance}m", font, (255, 255, 255), (SCREEN_WIDTH // 2, 270))

        btn_retry.draw(screen)
        btn_menu.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if btn_retry.is_clicked(event):
                score, distance = run_game(screen, settings) # Запуск заново
                persistence.save_score("Player", score, distance)
            if btn_menu.is_clicked(event):
                return

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main_menu()
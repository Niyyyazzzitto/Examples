import pygame

pygame.font.init()
font = pygame.font.SysFont("Verdana", 24)
big_font = pygame.font.SysFont("Verdana", 40)
small_font = pygame.font.SysFont("Verdana", 16)

def draw_text(surface, text, font_obj, color, center_pos):
    """Функция для вывода текста по центру"""
    text_surface = font_obj.render(text, True, color)
    rect = text_surface.get_rect(center=center_pos)
    surface.blit(text_surface, rect)

class Button:
    def __init__(self, x, y, w, h, text, color=(200, 200, 200), hover_color=(150, 150, 150)):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover_color = hover_color

    def draw(self, surface):
        # Проверяем, наведена ли мышка
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        
        # Рисуем кнопку и рамку
        pygame.draw.rect(surface, current_color, self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)
        
        # Рисуем текст
        draw_text(surface, self.text, font, (0, 0, 0), self.rect.center)

    def is_clicked(self, event):
        """Проверяет, кликнули ли по кнопке"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False
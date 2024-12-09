import math
import pygame

class BouncingText:
    def __init__(self, x_position, y_position, text="", font_size=34):
        self.text = text
        self.font_size = font_size
        self.x_position = x_position
        self.y_position = y_position
        self.bob_index = 0

    def display_text(self, screen):
        # Displays "Game Paused!" Start --------------------------------------------
        self.text_font = pygame.font.SysFont('Comic Sans MS', self.font_size)
        pause_surface = self.text_font.render(self.text, True, "white")
        pause_rect = pause_surface.get_rect(center=(self.x_position, self.y_position // 2 + 20* math.sin(self.bob_index / 100)))
        screen.blit(pause_surface, pause_rect)

        # Title Bobbing Logic Start ------------------------------------------------
        if self.bob_index < math.pi * 100:
            self.bob_index += 1
        else:
            self.bob_index = 0
        # Title Bobbing Logic End --------------------------------------------------

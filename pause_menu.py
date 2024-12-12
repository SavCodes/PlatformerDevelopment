import pygame
import math

# Refactor text display into a title class method for reusability

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.bob_index = 0
        self.width, self.height = pygame.display.get_window_size()
        self.my_font = pygame.font.SysFont('Comic Sans MS', self.width // 8)
        self.is_music_paused = False
        self.is_paused = False

    def event_checker(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.is_paused = not self.is_paused

    def display_pause_text(self, text_location, text_to_display="Testing"):
        text_surface = self.my_font.render(text_to_display, True, "black")
        pause_rect = text_surface.get_rect(center=(text_location[0], text_location[1]))
        self.screen.blit(text_surface, pause_rect)

    def display_pause_title(self, pause_text="Game Paused"):
        # Displays "Game Paused!" Start --------------------------------------------
        self.screen.fill((255,255,255))
        pause_surface = self.my_font.render(pause_text, True, "black")
        pause_rect = pause_surface.get_rect(center=(self.width // 2, self.height // 2 + 20* math.sin(self.bob_index / 100)))
        self.screen.blit(pause_surface, pause_rect)
        self.bob_text()

        # Display "Game Pause!" End ------------------------------------------------

    def bob_text(self):
        if self.bob_index < math.pi * 100:
            self.bob_index += 1
        else:
            self.bob_index = 0

    def run_pause_menu(self):
        self.display_pause_title()

import pygame
import math
import button


# Refactor text display into a title class method for reusability

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.bob_index = 0
        self.width, self.height = pygame.display.get_window_size()
        self.my_font = pygame.font.SysFont('Comic Sans MS', self.width // 8)
        self.is_music_paused = False
        self.is_paused = False
        self.create_menu_buttons()

    def event_checker(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.is_paused = not self.is_paused

    def display_pause_text(self, text_location, text_to_display="Testing"):
        text_surface = self.my_font.render(text_to_display, True, "black")
        pause_rect = text_surface.get_rect(center=(text_location[0], text_location[1]))
        self.screen.blit(text_surface, pause_rect)

    def bob_text(self):
        if self.bob_index < math.pi * 100:
            self.bob_index += 1
        else:
            self.bob_index = 0

    def run_pause_menu(self):
        self.display_pause_text((self.width // 2, self.height // 2), "Game Paused")

    def create_menu_buttons(self):
        level_editor_button = button.Button(self.screen, self.screen.width // 2, 40, text="Level Editor")
        save_game_button = button.Button(self.screen, self.screen.width // 2, 85, text="Save Game")
        quit_game_button = button.Button(self.screen, self.screen.width // 2, 130, text="Quit Game")

        self.button_list = [level_editor_button, save_game_button, quit_game_button]

    def display_menu_buttons(self):
        for _button in self.button_list:
            _button.display_button()

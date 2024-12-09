import pygame
import math

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

    def display_pause_title(self, pause_text="Game Paused"):
        # Displays "Game Paused!" Start --------------------------------------------
        self.screen.fill((255,255,255))
        pause_surface = self.my_font.render(pause_text, True, "black")
        pause_rect = pause_surface.get_rect(center=(self.width // 2, self.height // 2 + 20* math.sin(self.bob_index / 100)))
        self.screen.blit(pause_surface, pause_rect)
        self.bob_text()

        # Display "Game Pause!" End ------------------------------------------------


    def display_pause_instructions(self):
        # Displays Pause Instructions Start ----------------------------------------
        instructions_text = "Press Space to Pause/Unpause"
        instructions_size = self.width // 20
        my_font = pygame.font.SysFont('Comic Sans MS', instructions_size)
        instruction_surface = my_font.render(instructions_text, True, "white")
        instruction_rect = instruction_surface.get_rect(center=(self.width * 0.5, self.height * 0.7))
        self.screen.blit(instruction_surface, instruction_rect)
        # Display Pause Instructions End -------------------------------------------

    def display_move_instructions(self):
        # Displays Move Instructions Start -----------------------------------------
        move_instructions_text = "Use the arrow keys or w, a, s, d to move"
        move_instructions_size = self.width // 20
        my_font = pygame.font.SysFont('Comic Sans MS', move_instructions_size)
        move_instruction_surface = my_font.render(move_instructions_text, True, "black")
        move_instruction_rect = move_instruction_surface.get_rect(center=(self.width // 2, self.height * 0.77))
        self.screen.blit(move_instruction_surface, move_instruction_rect)
        # Display Move Instructions End --------------------------------------------

    def display_mute_instructions(self):
        # Displays Mute Instructions Start -----------------------------------------
        mute_instructions_text = "Press 'm' to Mute/Unmute Sound"
        mute_instructions_size = self.width // 20
        my_font = pygame.font.SysFont('Comic Sans MS', mute_instructions_size)
        mute_instruction_surface = my_font.render(mute_instructions_text, True, "black")
        mute_instruction_rect = mute_instruction_surface.get_rect(center=(self.width // 2, self.height * 0.84))
        self.screen.blit(mute_instruction_surface, mute_instruction_rect)
        # Display Mute Instructions End --------------------------------------------

    def bob_text(self):
        if self.bob_index < math.pi * 100:
            self.bob_index += 1
        else:
            self.bob_index = 0

    def run_pause_menu(self):
        self.display_pause_title()
        self.display_pause_instructions()
        self.display_move_instructions()
        self.display_mute_instructions()
        pygame.display.update()

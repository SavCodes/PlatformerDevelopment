import pygame
import world_generator
import level_files
from main import GAME_SCALE

class LevelObjective:
    def __init__(self, player, x_position, y_position, game_scale=1):
        self.player = player
        self.game_scale = game_scale
        self.x_position = x_position
        self.y_position = y_position
        self.color = (255,0,0)
        self.width = 32 * self.game_scale
        self.height = 32 *  GAME_SCALE * 2

    def display_objective(self, screen):
        self.objective_rect = pygame.Rect(self.x_position, self.y_position, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.objective_rect, 3)

    def check_objective_collision(self):
        if self.player.player_rect.colliderect(self.objective_rect):
            self.player.level_completed = True
            self.color = (255,255,255)


def check_level_complete(player_one, player_two):
    if player_one.level_completed and player_two.level_completed:

        # Advance player one to the next level and reset position
        player_one.current_level += 1
        print("PLAYER ONE CURRENT LEVEL: ", player_one.current_level)
        player_one.tile_set = world_generator.WorldGenerator(level_files.player_one_level_set[player_one.current_level], scale=GAME_SCALE).world_tiles
        print("new player one levels loaded")
        player_one.level_completed = False
        player_one.x_position = 300

        # Advance player two to the next level and reset position
        player_two.current_level += 1
        print("PLAYER TWO CURRENT LEVEL: ", player_two.current_level)
        player_two.tile_set = world_generator.WorldGenerator(level_files.player_two_level_set[player_two.current_level], scale=GAME_SCALE).world_tiles
        player_two.level_completed = False
        player_two.x_position = 900

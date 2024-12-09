import pygame

class Platform:
    def __init__(self, tile, x_position, y_position, is_collidable=True, scale=1):
        self.tile = tile
        self.tile_number = self.tile[self.tile.rfind("_") + 1:self.tile.rfind(".")]
        self.image = pygame.transform.scale_by(pygame.image.load(tile), scale).convert_alpha()
        self.width = 32 * scale
        self.height = 32 * scale
        self.platform_rect = pygame.Rect(x_position, y_position, self.width, self.height)
        self.x_position = x_position
        self.y_position = y_position
        self.is_collidable = is_collidable
        self.collision = None

    def __repr__(self):
        return f'"{self.tile}"'

    def draw_platform(self, screen):
        screen.blit(self.image, self.platform_rect)



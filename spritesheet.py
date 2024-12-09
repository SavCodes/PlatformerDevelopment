import pygame

class SpriteSheet:
    def __init__(self, sprite_sheet, scale=1.0, width=32, height=32):
        self.width = width
        self.height = height
        self.sprites = pygame.image.load(sprite_sheet)
        self.number_of_animations = int(sprite_sheet.split(".")[-2][-1])
        self.sprite_group = pygame.sprite.Group()
        self.scale = scale
        self.frame_list = [self.sprites.subsurface((self.width*index,0, self.width, self.height)) for index in range(self.number_of_animations)]
        self.frame_list = [pygame.transform.scale_by(frame, scale) for frame in self.frame_list]
        self.animation_index = 0
        self.animation_speed = 0.20

    def basic_animate(self, dampener=1):
        if self.animation_index < self.number_of_animations - 1:
            self.animation_index += self.animation_speed * dampener
        else:
            self.animation_index = 0

        return self.frame_list[int(self.animation_index)]
















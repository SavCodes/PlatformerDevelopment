import pygame
import math
from PIL import Image, ImageTransform

def generate_sway_sheet(file_path):
    # Load the original image_to_animate image
    image_to_animate = Image.open(file_path)
    image_to_animate = image_to_animate.resize((64,64))
    image_to_animate = image_to_animate.transpose(Image.ROTATE_180)
    # Create a list to store animation frames
    frames = []
    width, height = image_to_animate.size

    # Generate frames with transformations
    for angle in range(-10, 11, 1):  # Sway angles
        # Define a perspective transformation to sway the top
        coeffs = [
            1, angle / 100, 0,  # Top row is skewed => lower denominator = more sway
            0, 1, 0,  # Middle row remains stationary
            0, 0, 1  # Base remains fixed
        ]
        # Apply transformation
        frame = image_to_animate.transform(
            (width, height),
            Image.Transform.PERSPECTIVE,
            coeffs
        )
        frame = frame.transpose(Image.ROTATE_180)
        frames.append(frame)

    # Combine frames into a spritesheet
    spritesheet = Image.new("RGBA", (2 * width * len(frames), height))

    for i, frame in enumerate(frames):
        spritesheet.paste(frame, (i * width, 0))
        spritesheet.paste(frame, ((2* len(frames) - 1  - i) * width, 0))


    # Save the spritesheet
    spritesheet.save(f"{file_path[:file_path.rfind(".", 2)]}_spritesheet_TEST_{2*len(frames)}.png")

def generate_pulsate_sheet(file_path):
    # Load the original image and prepare it
    image_to_animate = Image.open(file_path)
    image_to_animate = image_to_animate.resize((64, 64))  # Resize to standard dimensions
    image_to_animate = image_to_animate.transpose(Image.ROTATE_180)  # Optional transformation

    # Get image dimensions
    width, height = image_to_animate.size

    # Create a list to store animation frames
    frames = []

    # Generate frames with pulsating transformations
    for scale_factor in range(-10, 11, 2):  # Scale factors for pulsation
        scale_factor /= 100  # Convert to a small percentage (e.g., -0.1 to 0.1)
        # Define perspective transformation coefficients for pulsation
        coeffs = [
            1 + scale_factor, 0, -width * scale_factor / 2,  # Horizontal scaling
            0, 1 + scale_factor, -height * scale_factor / 2,  # Vertical scaling
            0, 0, 1  # Perspective remains neutral
        ]
        # Apply transformation
        frame = image_to_animate.transform(
            (width, height),
            Image.Transform.PERSPECTIVE,
            coeffs
        )
        frame = frame.transpose(Image.ROTATE_180)  # Reverse rotation to restore original orientation
        frames.append(frame)

    # Combine frames into a spritesheet
    spritesheet = Image.new("RGBA", (2 * width * len(frames), height))

    for i, frame in enumerate(frames):
        spritesheet.paste(frame, (i * width, 0))
        spritesheet.paste(frame, ((2 * len(frames) - 1 - i) * width, 0))

    # Save the spritesheet
    spritesheet.save(f"{file_path[:file_path.rfind('.', 2)]}_spritesheet_PULSATE_{2 * len(frames)}.png")

def generate_ripple_sheet(file_path):
    # Load the original image and prepare it
    image_to_animate = Image.open(file_path)
    image_to_animate = image_to_animate.resize((64, 64))  # Resize to standard dimensions
    image_to_animate = image_to_animate.transpose(Image.ROTATE_180)  # Optional transformation

    # Get image dimensions
    width, height = image_to_animate.size

    # Create a list to store animation frames
    frames = []

    # Generate frames with pulsating transformations
    for scale_factor in range(-10, 11, 2):  # Scale factors for pulsation
        # Define perspective transformation coefficients for pulsation
        coeffs = [
            1 + scale_factor, 0, 0,  # Stretch horizontally
            0, 1, 0,  # No vertical scaling
            0, 0, 1
        ]
        # Apply transformation
        frame = image_to_animate.transform(
            (width, height),
            Image.Transform.PERSPECTIVE,
            coeffs
        )
        frame = frame.transpose(Image.ROTATE_180)  # Reverse rotation to restore original orientation
        frames.append(frame)

    # Combine frames into a spritesheet
    spritesheet = Image.new("RGBA", (2 * width * len(frames), height))

    for i, frame in enumerate(frames):
        spritesheet.paste(frame, (i * width, 0))
        spritesheet.paste(frame, ((2 * len(frames) - 1 - i) * width, 0))

    # Save the spritesheet
    spritesheet.save(f"{file_path[:file_path.rfind('.', 2)]}_spritesheet_RIPPLE_{2 * len(frames)}.png")

class SpriteSheet:
    def __init__(self, sprite_sheet, scale=1.0, width=32, height=32):
        self.width = width
        self.height = height
        self.sprites = pygame.image.load(sprite_sheet)
        self.number_of_animations = int(sprite_sheet[sprite_sheet.rfind("_")+1:sprite_sheet.rfind(".")])
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

class AnimatedTileManager:
    def __init__(self):
        self.animated_tiles = []  # List to store animated tile data

    def add_tile(self, sprite_sheet, location, animation_speed=0.03):
        """Add a new animated tile."""
        self.animated_tiles.append({
            "sprite_sheet": sprite_sheet,
            "location": location,
            "animation_speed": animation_speed
        })

    def draw_tiles(self, surface):
        """Draw all animated tiles to the surface."""
        for tile in self.animated_tiles:
            frame = tile["sprite_sheet"].basic_animate(0.2)
            surface.blit(frame, tile["location"])

generate_ripple_sheet("./game_assets/animated_tiles/bush.png")




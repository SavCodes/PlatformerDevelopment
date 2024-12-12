import pygame
import time

class Chatbox:
    def __init__(self, text, location, color=(50,50,50)):
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont("comicsans", 30)
        self.x = location[0]
        self.y = location[1]

    def update_text(self, text):
        self.text = text


    def rolling_text(self, surface, delay=0.1):
        displayed_text = ""
        for char in self.text:
            displayed_text += char

            # Create Surfaces
            text_surface = self.font.render(displayed_text, True, self.color)
            rect_surface = pygame.Rect((self.x, self.y), text_surface.get_size())
            outline_surface = pygame.Rect((self.x, self.y), (text_surface.get_size()[0] + 10, text_surface.get_size()[1] + 10))

            # Draw Surfaces
            pygame.draw.rect(surface, (0, 255, 255), outline_surface)
            pygame.draw.rect(surface, (255, 0, 0), rect_surface)
            surface.blit(text_surface, (self.x, self.y))

            # Update display and wait
            pygame.display.update()
            time.sleep(delay)  # Delay to create the typing effect


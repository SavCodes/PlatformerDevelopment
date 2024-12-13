import pygame
import time
import npc_chat_logs

class Chatbox:
    def __init__(self, character, chat_tree, location, color=(50,50,50)):
        self.displayed_text = ""
        self.text_index = 0
        self.dialouge_index = 0


        self.character_chat_tree = npc_chat_logs.chat_logs[character][chat_tree]
        self.text = self.character_chat_tree[self.dialouge_index]

        self.color = color
        self.font = pygame.font.SysFont("comicsans", 30)
        self.x, self.y = location
        self.is_displaying = True


    def roll_text(self, surface, delay=0.1):
         # Create Surfaces
        text_surface = self.font.render(self.displayed_text, True, self.color)
        rect_surface = pygame.Rect((self.x, self.y), text_surface.get_size())

        # Draw Surfaces
        pygame.draw.rect(surface, (255, 0, 0), rect_surface)
        surface.blit(text_surface, (self.x, self.y))

        # Update display and wait
        pygame.display.update()
        time.sleep(delay)  # Delay to create the typing effect
        if self.text_index <= len(self.text) - 1:
            self.displayed_text += self.text[self.text_index]
            self.text_index += 1

    def progress_chat(self):
        if self.text_index < len(self.text) - 1 and self.is_displaying:
            self.displayed_text = self.text
            self.text_index = len(self.text)

        elif self.dialouge_index < len(self.character_chat_tree) - 1 and self.is_displaying:
            self.text_index = 0
            self.displayed_text = ""
            self.dialouge_index += 1
            self.text = self.character_chat_tree[self.dialouge_index]
        else:
            self.escape_chat()

    def escape_chat(self):
        self.is_displaying = False


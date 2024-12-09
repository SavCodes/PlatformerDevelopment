import pygame

class Button:
    def __init__(self, screen, x, y, width, height, text_color="white", text="testing", font_size=12):
        #================ DIMENSION ATTRIBUTES =====================
        self.x_position = x
        self.y_position = y
        self.width = width
        self.height = height
        self.is_pressed = False
        self.is_hovering = False

        #================ DISPLAY ATTRIBUTES =======================
        self.screen = screen
        self.text_color = text_color
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.SysFont("comicsans", self.font_size)

    def display_button(self, color=(50,50,50)):
        button_text = self.font.render(self.text, True, "white")
        button_rect = pygame.Rect(0, 0, self.width, self.height)
        button_rect.center = (self.x_position, self.y_position)
        pygame.draw.rect(self.screen, color, button_rect)
        self.screen.blit(button_text, button_rect)

    def check_pressed(self, mouse_x, mouse_y):
        if self.x_position - self.width / 2 < mouse_x < self.x_position + self.width / 2:
            if self.y_position - self.height / 2 < mouse_y < self.y_position + self.height / 2:
                self.display_hover_effect()
                if pygame.mouse.get_just_pressed()[0]:
                    self.is_pressed = True
                    print("Pressed: ", self.text)
        else:
            self.is_pressed = False

    def display_hover_effect(self):
        button_rect = pygame.Rect(0, 0, self.width * 1.05, self.height * 1.05)
        button_rect.center = (self.x_position, self.y_position)
        pygame.draw.rect(self.screen, (255,255,255), button_rect, int(self.width * 0.05))

    def set_text(self, text):
        self.text = text

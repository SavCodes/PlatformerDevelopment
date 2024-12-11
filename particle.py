import pygame
import random



screen_width, screen_height = 1248, 640


class Particle:
    def __init__(self, x_pos, y_pos):
        self.position = pygame.math.Vector2(x_pos, y_pos)

    def drift(self):
        self.position += (random.randint(-3,-1)/5, random.randint(2, 4)/5)

    def display(self, screen):
        pygame.draw.circle(screen, (50, 100, 50), self.position, 1)

    def reset(self, player):
        if  self.position[0] <= player.position[0] - screen_width / 2:
            self.position[0] = player.position[0] + screen_width / 2
        elif self.position[0] > player.position[0] + screen_width:
            self.position[0] = random.randint(-screen_width//2, screen_width//2) + player.position[0]
        if self.position[1] >= screen_height:
            self.position[1] = 0

def create_particles(num_particles=100):
    return  [Particle(random.randint(0, screen_width), random.randint(0,screen_height)) for i in range(num_particles)]

def render_particles(screen, particle_list, player):
    for particle in particle_list:
        particle.display(screen)
        particle.drift()
        particle.reset(player)

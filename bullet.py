import pygame
from pygame.sprite import Sprite
from settings import *


class Bullet(Sprite):
    def __init__(self, screen, player):
        super().__init__()
        self.screen = screen
        self.player = player
        self.direction = self.player.turn
        self.rect = pygame.Rect(self.player.x, self.player.y, bullet_width, bullet_height)
        self.rect.top = self.player.rect.top
        self.bullet_speed = 25

        self.y_b = float(self.rect.y)
        self.x_b = float(self.rect.x)

    @property
    def bullets_pos(self):
        return self.x_b, self.y_b

    def update(self):
        if self.direction == 'up':
            self.y_b -= self.bullet_speed
            self.rect.y = self.y_b
        elif self.direction == 'down':
            self.y_b += self.bullet_speed
            self.rect.y = self.y_b
        elif self.direction == 'left':
            self.x_b -= self.bullet_speed
            self.rect.x = self.x_b
        elif self.direction == 'right':
            self.x_b += self.bullet_speed
            self.rect.x = self.x_b

    def draw_bullet(self):
        pygame.draw.rect(self.screen, RED, self.rect)

    def detect_collisions(self, walls):
        hit_index = self.rect.collidelistall(walls)
        if hit_index:
            return 1
# ball.py

import pygame
from settings import WHITE, BALL_RADIUS, BALL_SPEED_X, BALL_SPEED_Y

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - BALL_RADIUS, y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)

    def reset(self, x, y):
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y - self.rect.height // 2
        self.speed_x = -self.speed_x  # Change direction when resetting

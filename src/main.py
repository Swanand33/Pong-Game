# main.py

import pygame
import sys
from settings import *
from paddle import Paddle
from ball import Ball

def main():
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pong')

    # Create game objects
    player1 = Paddle(30, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2)
    player2 = Paddle(SCREEN_WIDTH - 40, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 74)

    score1 = 0
    score2 = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.rect.top > 0:
            player1.move(up=True)
        if keys[pygame.K_s] and player1.rect.bottom < SCREEN_HEIGHT:
            player1.move(up=False)
        if keys[pygame.K_UP] and player2.rect.top > 0:
            player2.move(up=True)
        if keys[pygame.K_DOWN] and player2.rect.bottom < SCREEN_HEIGHT:
            player2.move(up=False)

        # Move the ball
        ball.move()

        # Ball collision with top/bottom
        if ball.rect.top <= 0 or ball.rect.bottom >= SCREEN_HEIGHT:
            ball.speed_y = -ball.speed_y

        # Ball collision with paddles
        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            ball.speed_x = -ball.speed_x

        # Ball goes out of bounds
        if ball.rect.left <= 0:
            score2 += 1
            ball.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        if ball.rect.right >= SCREEN_WIDTH:
            score1 += 1
            ball.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Fill the screen with black color
        screen.fill(BLACK)

        # Draw paddles and ball
        player1.draw(screen)
        player2.draw(screen)
        ball.draw(screen)

        # Display the scores
        score_text1 = font.render(str(score1), True, WHITE)
        screen.blit(score_text1, (250, 10))
        score_text2 = font.render(str(score2), True, WHITE)
        screen.blit(score_text2, (510, 10))

        # Update the screen
        pygame.display.flip()

        # Ensure the game runs at 60 frames per second
        clock.tick(FPS)

if __name__ == '__main__':
    main()

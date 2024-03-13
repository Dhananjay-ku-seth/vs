import pygame
import time

# Initialize pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Snake settings
snake_speed = 15
snake_block = 10

# Initialize snake position and direction
x, y = width / 2, height / 2
x_change, y_change = 0, 0

# Main game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = snake_block

    # Update snake position
    x += x_change
    y += y_change

    # Clear the screen
    screen.fill(WHITE)

    # Draw the snake
    pygame.draw.rect(screen, BLACK, [x, y, snake_block, snake_block])

    # Update the display
    pygame.display.update()

    # Limit snake speed
    clock.tick(snake_speed)

# Quit pygame
pygame.quit()

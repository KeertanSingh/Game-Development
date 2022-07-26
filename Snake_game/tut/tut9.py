# Snake game - Creating ground or canvas for snake

# velocity

# importing module
import pygame

pygame.init()

# Colors
white = (204, 194, 194)
red = (227, 14, 14)
black = (0, 0, 0)
yellow = (117, 87, 5)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption(" 🐍Snake Game🐍")
# Updating display
pygame.display.update()

# Game specific variables
exit_game = False  # when this variable will change into True then the game will be quit!!
game_over = False  # When this variable will change into True then the game will be over!!
snake_x = 45  # initial position of snake at x-axis
snake_y = 65  # initial position of snake at y-axis
velocity_x = 4
velocity_y = 4
snake_size = 20  # size of snake
fps = 30
clock = pygame.time.Clock()

# Game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("GAME IS EXIT!")
            exit_game = True
        if event.type == pygame.KEYDOWN:
            # Moving snake into all directions
            if event.key == pygame.K_RIGHT:
                snake_x += 10
            if event.key == pygame.K_LEFT:
                snake_x -= 10
            if event.key == pygame.K_UP:
                snake_y -= 10
            if event.key == pygame.K_DOWN:
                snake_y += 10

    snake_x +=velocity_x
    snake_y +=velocity_y
    gameWindow.fill(white)  # Color
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])  # Creating rectangle as snake head
    pygame.display.update()  # Updating window
    clock.tick(fps)

pygame.quit()  # Pygame exit
quit()  # Program exit

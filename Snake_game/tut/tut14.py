# high score
# Snake game - Creating ground or canvas for snake


# importing module
import pygame
import random

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
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def ploat_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Game loop
def game_loop():
    # Game specific variables
    exit_game = False  # when this variable will change into True then the game will be quit!!
    game_over = False  # When this variable will change into True then the game will be over!!
    snake_x = 45  # initial position of snake at x-axis
    snake_y = 65  # initial position of snake at y-axis
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width / 2)  # Creating food position at x-axis
    food_y = random.randint(20, screen_height / 2)  # creating food position at y-axis
    snake_size = 20  # size of snake
    fps = 60
    score = 0
    initial_velocity = 3
    snake_list = []
    snake_length = 1
    with open("high_score.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:

            gameWindow.fill(white)
            text_screen("Game over! Press enter to continue", red, 150, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    # Moving snake into all directions
                    if event.key == pygame.K_RIGHT:
                        velocity_x = initial_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -initial_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -initial_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = initial_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
                score += 10

                food_x = random.randint(20, screen_width / 2)  # Creating food position at x-axis
                food_y = random.randint(20, screen_height / 2)  # creating food position at y-axis
                snake_length += 2

            gameWindow.fill(white)  # Color
            text_screen("Score: " + str(score) + "  Highscore: " + str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])  # food

            if score > int(highscore):
                highscore = score
                with open("high_score.txt", "w") as f:
                    f.write(str(score))

            head = [snake_x, snake_y]
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            ploat_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()  # Updating window
        clock.tick(fps)

    pygame.quit()  # Pygame exit
    quit()  # Program exit


game_loop()

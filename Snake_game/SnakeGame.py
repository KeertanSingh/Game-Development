# snake game

# importing module
import pygame
import random
import os

# Music
pygame.mixer.init()
pygame.init()

# Colors
white = (204, 194, 194)
red = (227, 14, 14)
black = (0, 0, 0)
yellow = (250, 209, 62)
orange = (245, 76, 15)
blue = (30, 176, 230)
brown = (64, 49, 6)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# background image
bgimg = pygame.image.load('images/bgimg.png')
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption(" 🐍Snake Game by keerat🐍")
# Updating display
pygame.display.update()
# font = pygame.font.SysFont(None, 60)
font = pygame.font.Font("amatic/font.ttf", 55)
clock = pygame.time.Clock()


def music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.mixer.stop()


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def ploat_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((194, 181, 235))
        gameWindow.blit(
            pygame.transform.scale(pygame.image.load('images/welcome.png'), (screen_width, screen_height)).convert_alpha(),
            (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('music/back.mp3')
                    pygame.mixer.music.play(loops=100)
                    game_loop()
        pygame.display.update()
        clock.tick(60)


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
    initial_velocity = 4
    snake_list = []
    snake_length = 1
    # Check if high_score file exist
    if not os.path.exists("high_score.txt"):
        with open("high_score.txt", "w") as f:
            f.write("0")
    with open("high_score.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            gameWindow.blit(pygame.transform.scale(pygame.image.load('images/gameover.png'),
                                                   (screen_width, screen_height)).convert_alpha(), (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
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

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 10

                food_x = random.randint(20, screen_width / 2)  # Creating food position at x-axis
                food_y = random.randint(20, screen_height / 2)  # creating food position at y-axis
                snake_length += 2

            gameWindow.fill(white)  # Color
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  Highscore: " + str(highscore), brown, 500, 5)
            pygame.draw.rect(gameWindow, yellow, [food_x, food_y, snake_size, snake_size])  # food

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
                music("music/gameover.mp3")

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                music("music/gameover.mp3")

            ploat_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()  # Updating window
        clock.tick(fps)

    pygame.quit()  # Pygame exit
    quit()  # Program exit


welcome()

import pygame  # import pygame
from pygame.locals import *
import random

pygame.init()  # initializing the pygame module

font = pygame.font.Font("font.ttf", 35)
clock = pygame.time.Clock()
screen_width = 600  # screen width
screen_height = 600  # screen height
gameWindow = pygame.display.set_mode((screen_width,screen_height))
brown = (64, 49, 6)
# score = 0
def music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.mixer.stop()


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((194, 181, 235))
        gameWindow.blit( pygame.transform.scale(pygame.image.load('welcome.png'), (screen_width,
        screen_height)).convert_alpha(), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # pygame.mixer.music.load('music/back.mp3')
                    # pygame.mixer.music.play(loops=100)
                    game_loop()
        pygame.display.update()
        clock.tick(60)


def game_loop():
    # Game variable
    running = True  # for loop
    screen_width = 600  # screen width
    screen_height = 600  # screen height
    background_color = (30, 207, 27)  # green color
    road_width = int(screen_width / 1.6)  # width of the road
    road_color = (50, 50, 50)
    roadmark_width = int(screen_width / 80)
    roadmark_color = (255, 240, 60)
    sideLine_color = (255, 255, 255)
    right_lane = screen_width / 2 + road_width / 4
    left_lane = screen_width / 2 - road_width / 4
    speed = 1
    score = 0
    # fps = 60
    # game_over = True
    # white = (255, 255, 255)

    # Screen
    pygame.display.set_caption("Car Racing game")  # title of the game
    screen = pygame.display.set_mode((screen_width, screen_height))  # creating screen
    screen.fill(background_color)  # background color of screen

    # apply changes
    pygame.display.update()  # update the screen

    # Load player images
    car = pygame.image.load("car1.png")
    car_loc = car.get_rect()
    car_loc.center = right_lane, screen_height * 0.8

    # Load enemy images
    car2 = pygame.image.load("othecar.png")
    car2_loc = car2.get_rect()
    car2_loc.center = left_lane, screen_height * 0.2

    counter = 0



    # Game loop
    while running:
        counter += 1
        if counter == 5000:
            # print(counter)
            speed += 0.15
            counter = 0
            # print("Level up", speed)
        # animate enemy vehicale
        car2_loc[1] += speed
        if car2_loc[1] > screen_height:
            # car2_loc[1] = -600
            if random.randint(0, 1) == 0:
                car2_loc.center = right_lane, -1000
            else:
                car2_loc.center = left_lane, -1000
        # end game
        if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 200:
            print("Game over! you lost!")
            break
        if car_loc[1] == -int(car2_loc[1]):
            score += 1
            text_screen("Score: " + str(score), brown, 5, 5)
            # print(f"your score: {score}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_a, K_LEFT]:
                    car_loc = car_loc.move([-int(road_width / 2), 0])
                if event.key in [K_d, K_RIGHT]:
                    car_loc = car_loc.move([int(road_width / 2), 0])
        # draw graphics
        # Drawing road
        pygame.draw.rect(
            screen,
            road_color,
            (screen_width / 2 - road_width / 2, 0, road_width, screen_height))

        # Draw road mark
        pygame.draw.rect(
            screen,
            roadmark_color,
            (screen_width / 2 - roadmark_width / 2, 0, roadmark_width, screen_height)
        )
        # Drawing left-side line of the road
        pygame.draw.rect(
            screen,
            sideLine_color,
            (screen_width / 2 - road_width / 2 + roadmark_width * 2, 0, roadmark_width, screen_height)
        )
        # Drawing Right-side line of the road
        pygame.draw.rect(
            screen,
            sideLine_color,
            (screen_width / 2 + road_width / 2 - roadmark_width * 3, 0, roadmark_width, screen_height)
        )

        screen.blit(car, car_loc)
        screen.blit(car2, car2_loc)
        pygame.display.update()  # update the screen
        # clock.tick(fps)

    pygame.quit()  # quit the pygame

# game_loop()
welcome()
exit()  # exit the program

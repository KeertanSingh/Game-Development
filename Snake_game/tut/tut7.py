# Event types and key press handling in pygame


# importing modules
import pygame  # import pygame

pygame.init()  # importing all the pygame module

# Creating window
gameWindow = pygame.display.set_mode((500, 300))  # creating display window

# creating game title
pygame.display.set_caption("My first game!")  # title set on game window

# Game specific variables
exit_game = False  # when this variable will change into True then the game will be quit!!
game_over = False  # When this variable will change into True then the game will be over!!

# Creating a game loop
# Game loop = loop which will run until we are not quiting game.
while not exit_game:  # This loop will continue until the exit_game is False:
    for event in pygame.event.get():  # pygame.event.get() = get events from the queue
        if event.type == pygame.QUIT:
            print("Game exit!!")
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("you have pressed right arrow key!!")


pygame.quit()  # to uninitialize all pygame modules
quit()  # to exit from python program

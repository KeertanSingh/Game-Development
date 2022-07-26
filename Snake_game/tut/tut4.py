# Game specific variable in pygame

# importing modules
import pygame  # import pygame

pygame.init()  # importing all the pygame module

# Creating window
gameWindow = pygame.display.set_mode((1000, 500))  # creating display window

# creating game title
pygame.display.set_caption("My first game!")  # title set on game window

# Game specific variables
exit_game = False  # when this variable will change into True then the game will be quit!!
game_over = False  # When this variable will change into True then the game will be over!!

# För att importera slumpmässiga värden och andra moduler
pip install pygame
pip3 install pygame

import random
import sys
import pygame
from pygame.locals import *

# Globala variabler för spelet
window_width = 600
window_height = 499

# Skapa ett Pygame-fönster
window = pygame.display.set_mode((window_width, window_height))
elevation = window_height * 0.8
game_images = {}
framepersecond = 32

# Ladda bilder från de uppladdade filerna
pipe_image = pygame.image.load('/mnt/data/pipe.jpg')
background_image = pygame.image.load('/mnt/data/skylevel.png')
birdplayer_image = pygame.image.load('/mnt/data/bird.png')
sealevel_image = pygame.image.load('/mnt/data/sealevel.jpg')

# Initiera spelet
def initialize_game():
    pygame.init()
    framepersecond_clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')

    # Ladda bilder
    game_images['background'] = background_image.convert()
    game_images['bird'] = birdplayer_image.convert_alpha()
    game_images['pipe'] = pipe_image.convert_alpha()
    game_images['base'] = sealevel_image.convert_alpha()

    return framepersecond_clock

# Funktion för att generera slumpmässiga höjder för rören
def create_pipe():
    pipe_height = game_images['pipe'].get_height()
    offset = window_height / 3
    y2 = offset + random.randrange(0, int(window_height - game_images['base'].get_height() - 1.2 * offset))
    pipeX = window_width + 10
    y1 = pipe_height - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},  # Övre rör
        {'x': pipeX, 'y': y2}    # Nedre rör
    ]
    return pipe

# Huvudspelloop
def game_loop():
    bird_x = int(window_width / 5)
    bird_y = int(window_height / 2)
    bird_y_change = 0
    base_x = 0

    # Skapa startvärden för rören
    pipe_velocity_x = -4
    new_pipe1 = create_pipe()
    new_pipe2 = create_pipe()

    upper_pipes = [
        {'x': window_width + 200, 'y': new_pipe1[0]['y']},
        {'x': window_width + 400, 'y': new_pipe2[0]['y']}
    ]
    lower_pipes = [
        {'x': window_width + 200, 'y': new_pipe1[1]['y']},
        {'x': window_width + 400, 'y': new_pipe2[1]['y']}
    ]

    while True:
        # Hantera användarinmatning
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                bird_y_change = -9  # Uppåt kraft när spelaren trycker
        bird_y_change += 1  # Gravitation
        bird_y = bird_y + bird_y_change

        # Uppdatera rörens positioner
        for upper_pipe, lower_pipe in zip(upper_pipes, lower_pipes):
            upper_pipe['x'] += pipe_velocity_x
            lower_pipe['x'] += pipe_velocity_x

        # Rita bakgrund och rör
        window.blit(game_images['background'], (0, 0))
        for upper_pipe, lower_pipe in zip(upper_pipes, lower_pipes):
            window.blit(game_images['pipe'], (upper_pipe['x'], upper_pipe['y']))
            window.blit(game_images['pipe'], (lower_pipe['x'], lower_pipe['y']))

        # Rita fågeln
        window.blit(game_images['bird'], (bird_x, bird_y))

        pygame.display.update()

        # Begränsa hastigheten för att spelet inte ska gå för snabbt
        framepersecond_clock.tick(framepersecond)

if __name__ == "__main__":
    framepersecond_clock = initialize_game()
    game_loop()

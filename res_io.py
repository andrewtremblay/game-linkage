import os, sys
import pygame

def load_image(name):
    "loads cursor image"
    fullname = os.path.join('res', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image:', fullname)
        raise SystemExit
    image = image.convert_alpha()
    return image, image.get_rect()

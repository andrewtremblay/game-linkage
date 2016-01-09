import os, sys
import pygame

def load_image(name, new_size=None):
    "loads cursor image"
    fullname = os.path.join('res', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image:', fullname)
        raise SystemExit
    image = image.convert_alpha()
    if new_size is not None:
        image = pygame.transform.scale(image, new_size)
    return image, image.get_rect()

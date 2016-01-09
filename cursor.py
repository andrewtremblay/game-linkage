import pygame
import debug, res_io
import game_globals #cursor size

class Cursor(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if debug.hide_native_cursor:
            pygame.mouse.set_visible(0)
        self.cursor_state = 0
        self.image, self.rect = res_io.load_image('cursor_hand.png', new_size=(15,15))

    def update(self):
        "move the fist based on the mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos

    def set_cursor_state(self, new_hover=None, new_pressed=None):
        "update the cursor display"
        hover_state = new_hover
        pressed_state = new_pressed
        if(new_pressed is not None):
            print("new_pressed")
        elif(new_hover is not None):
            print("new_hover")

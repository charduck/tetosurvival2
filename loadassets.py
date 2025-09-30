try:
    import pygame
except ImportError:
    print("Import Error caught.")

def load_sprite(imgname, filetype):
    sprite = pygame.image.load("assets/sprites/" + imgname + "." + filetype).convert_alpha()
    return sprite

def load_image(imgname, filetype):
    image = pygame.image.load("assets/images/" + imgname + "." + filetype).convert_alpha()
    return image
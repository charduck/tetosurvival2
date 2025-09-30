try:
    import pygame
    import math
    import random
    import json
    import sys
    import time
    import loadassets as la
    import loadsettings as ls
except ImportError:
    print("Error importing required libraries.")

pygame.init()
clock = pygame.time.Clock()

settings = ls.loadSettings()
resolution = settings["resolution"]
screenWidth, screenHeight = resolution
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

tetoImage = la.load_sprite("teto", "webp")
mikuImage = la.load_sprite("miku", "webp")
neruImage = la.load_sprite("neru", "webp")

pygame.display.set_caption("Teto Survival")
pygame.display.set_icon(tetoImage)

running = True

virtualWidth = screenWidth
virtualHeight = screenHeight
virtualSurface = pygame.Surface((virtualWidth, virtualHeight))

# ----------- LOADING SCREEN START ----------- #

splashImage = la.load_image("splash", "png")

    # ----------- LOADING ASSETS ----------- #

        # ----------- LOADING AUDIO ----------- #

        # ----------- LOADING SPRITES ----------- #



        # ----------- LOADING MENU ASSETS ----------- #

    # ----------- LOADING DATA ----------- #

        # ----------- LOADING DIALOGUE ----------- #

storyActive = False
curentDialogueIndex = 0
waitingForInput = False

# ----------- LOADING SCREEN END ----------- #

# ----------- MAIN MENU ----------- #
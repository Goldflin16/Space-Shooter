import pygame
import os
import random

pygame.init()

size_window = (1200, 800)
size_hero = (80, 120)
size_bot = (74, 60)
size_bg = (1837, 1200)

colors = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "BLUE": (0, 50, 200)
}
FPS = 120



bullet_list_hero = list()
bullet_list_bot = list()

abs_path = os.path.abspath(__file__ + "/..")  

hero_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero1.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero2.png")), size_hero),
]

bot_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "bot1.png")), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "bot2.png")), size_bot),
    

]
bg_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "bg.png")), size_bg),90)

hp_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "heart.png")), (20, 20))
import pygame
import random
from colorama import *

pygame.mixer.unit()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
pygame.init()

counter_colour = (50, 205, 50)
background = (46, 139, 87)
worm_col =(255, 105, 180)
meal = (165, 42, 42)

dis_width = 1000
dis_height = 800

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Chervjachok")

worm_lenght = 10
worm_speed = 4

font_style = pygame.font.SysFont("Lexend", 25)
score_font = pygame.font.SysFont("Lexend", 35)

def Count(score)
    value = score_font.render("Score: " + str(score),True counter_colour)
    dis.blit(value, [340, 100]) # координаты строчки на экране

def worm_eating(worm_lenght,worm_list)
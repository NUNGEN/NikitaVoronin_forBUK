import pygame
import random
import time
#import sys
#import os
from colorama import *

pygame.init()
pygame.mixer.init()
music_path = "C:\\Users\\opilane\\source\\repos\\MUSIC FOLDER\\793440_Pest-of-The-Cosmos"
pygame.mixer.music.load(music_path)  #C:\\Users\\opilane\\source\\repos\\MUSIC FOLDER\\793440_Pest-of-The-Cosmos
pygame.mixer.music.play(loops=1, fade_ms=2000)
pygame.mixer.music.set_volume(1.0)

counter_colour = (50, 205, 50)
background = (46, 139, 87)
worm_colour = (255, 105, 180)
meal = (165, 42, 42)

dis_width = 1100
dis_height = 900

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Chervjachok")

clock = pygame.time.Clock()

worm_length = 10
worm_speed = 4

font_style = pygame.font.SysFont("Monospace", 25)
score_font = pygame.font.SysFont("Monospace", 35)

def Count(score):
    value = score_font.render("Score: " + str(score),True, counter_colour)
    dis.blit(value, [340, 100]) # координаты строчки на экране

def worm_eating(worm_length, worm_list):
    for x in worm_list:
       pygame.draw.rect(dis, worm_colour, [x[0], x[1], worm_length, worm_length])  
 #pygame.draw.rect(dis, worm_colour, [x[0], x[1], worm_length])   
def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
def gameloop():
    game_over = False
    game_close = False
    
    x1 = dis_width / 2
    y1 = dis_height / 2
    
    x1_change = 0
    y1_change = 0
    
    worm_list = []
    exact_worm_length = 1
    foodx = round(random.randrange(0, dis_width - worm_length) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - worm_length) / 10.0) * 10.0
    
    while not game_over:
        
        while game_close == True:
            dis.fill(background)
            message("DEFEATED , R - RESTART, Q - QUIT", (204, 42, 8))
            Count(exact_worm_length - 1)
            pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: #quit
                    game_over = True
                    game_close = False
                if event.key == pygame.K_r: #restart
                    gameloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_a:
                    x1_change = -worm_length
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = worm_length
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -worm_length
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = worm_length
                    x1_change = 0
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_close = True
    x1 += x1_change
    y1 += y1_change
    dis.fill(background)
    pygame.draw.rect(dis, meal, [foodx, foody, worm_length, worm_length])
    worm_head = []
    worm_head.append(x1)
    worm_head.append(y1)
    worm_list.append(worm_head)
    if len(worm_list) > exact_worm_length:
        del worm_list[0]
        
    for x in worm_list[:-1]:
        if x == worm_head:
            game_close = True
    worm_eating(worm_length, worm_list)
    Count(exact_worm_length -1)
    
    pygame.display.update()
    
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, dis_width - worm_length) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - worm_length) / 10.0) * 10.0
        exact_worm_length += 1
        
    
    clock.tick(worm_speed)
    

    pygame.quit()
    pygame.mixer.music.stop()
    quit()
    
gameloop()

#Run.WormTheGame.py    
 #   worm_eating(snake_block,)





# import pygame
# import random
# import time
# from colorama import *  # Не используется в коде, можно не импортировать
# 
# # Инициализация Pygame
# pygame.init()
# 
# # Инициализация микшера для работы с музыкой
# pygame.mixer.init()
# 
# # Путь к файлу музыки (укажи правильный путь)
# music_path = "793440_Pest-of-The-Cosmos.mp3"
# pygame.mixer.music.load(music_path)  # Загрузка музыки
# pygame.mixer.music.play(loops=1, fade_ms=2000)  # Воспроизведение музыки с эффектом
# pygame.mixer.music.set_volume(1.0)  # Установка громкости
# 
# # Цвета
# counter_colour = (50, 205, 50)
# background = (46, 139, 87)
# worm_colour = (255, 105, 180)
# meal = (165, 42, 42)
# 
# # Разрешение экрана
# dis_width = 1100
# dis_height = 900
# 
# # Настройка экрана
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption("Chervjachok")
# 
# clock = pygame.time.Clock()
# 
# worm_length = 10
# worm_speed = 4
# 
# font_style = pygame.font.SysFont("Monospace", 25)
# score_font = pygame.font.SysFont("Monospace", 35)
# 
# # Функция для вывода счета
# def Count(score):
#     value = score_font.render("Score: " + str(score), True, counter_colour)
#     dis.blit(value, [340, 100])  # координаты строчки на экране
# 
# # Функция для рисования червя
# def worm_eating(worm_length, worm_list):
#     for x in worm_list:
#         pygame.draw.rect(dis, worm_colour, [x[0], x[1], worm_length, worm_length])
# 
# # Функция для отображения сообщения
# def message(msg, colour):
#     mesg = font_style.render(msg, True, colour)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
# 
# # Главный игровой цикл
# def gameloop():
#     game_over = False
#     game_close = False
# 
#     x1 = dis_width / 2
#     y1 = dis_height / 2
# 
#     x1_change = 0
#     y1_change = 0
# 
#     worm_list = []
#     exact_worm_length = 1
#     foodx = round(random.randrange(0, dis_width - worm_length) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - worm_length) / 10.0) * 10.0
# 
#     while not game_over:
# 
#         while game_close == True:
#             dis.fill(background)
#             message("DEFEATED , R - RESTART, Q - QUIT", (204, 42, 8))
#             Count(exact_worm_length - 1)
#             pygame.display.update()
# 
#         for event in pygame.event.get():  # Объединяем оба блока обработки событий
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_q:  # quit
#                     game_over = True
#                     game_close = False
#                 if event.key == pygame.K_r:  # restart
#                     gameloop()
#                 if event.key == pygame.K_a:
#                     x1_change = -worm_length
#                     y1_change = 0
#                 elif event.key == pygame.K_d:
#                     x1_change = worm_length
#                     y1_change = 0
#                 elif event.key == pygame.K_w:
#                     y1_change = -worm_length
#                     x1_change = 0
#                 elif event.key == pygame.K_s:
#                     y1_change = worm_length
#                     x1_change = 0
# 
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
# 
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(background)
# 
#         pygame.draw.rect(dis, meal, [foodx, foody, worm_length, worm_length])
#         worm_head = []
#         worm_head.append(x1)
#         worm_head.append(y1)
#         worm_list.append(worm_head)
#         if len(worm_list) > exact_worm_length:
#             del worm_list[0]
# 
#         for x in worm_list[:-1]:
#             if x == worm_head:
#                 game_close = True
# 
#         worm_eating(worm_length, worm_list)
#         Count(exact_worm_length - 1)
# 
#         pygame.display.update()
# 
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - worm_length) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - worm_length) / 10.0) * 10.0
#             exact_worm_length += 1
# 
#         clock.tick(worm_speed)
# 
#     pygame.quit()
#     pygame.mixer.music.stop()
#     quit()
# 
# gameloop()

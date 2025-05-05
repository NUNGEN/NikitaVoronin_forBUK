#важные библиотеки pygame и random
import pygame 
import random 

pygame.init()

# основные цвета в игре
counter_colour = (50, 205, 50)
background = (46, 139, 87)
worm_colour = (255, 105, 180)
meal = (165, 42, 42)

# Размеры экрана 1100 на 900 пикселей
dis_width = 1100
dis_height = 900
worm_length = 10 # размер одного сегменнта червя в пикселях на экране
worm_speed = 12

# Окно запуска
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Chervjachok")

clock = pygame.time.Clock()

# Шрифты
font_style = pygame.font.SysFont("Monospace", 25)
score_font = pygame.font.SysFont("Monospace", 35)

#Вывод счёта на экран 
def Count(score):
    value = score_font.render("Score: " + str(score), True, counter_colour)
    dis.blit(value, [340, 100])

def worm_eating(worm_length, worm_list):
    for x in worm_list:
        pygame.draw.rect(dis, worm_colour, [x[0], x[1], worm_length, worm_length])

def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameloop():
#перемещение червя и реализация поражения с выходом из игры
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    worm_list = []#Список, который содержит и обновляет сегменты длины червя 
    exact_worm_length = 1#Значение текущей длины червя
    worm_speed = 12#скорость червя по умолчанию
#деление на 10 и умножение потом на 10, чтобы координаты  сеткой,
#по которой двигается червь (шаг и ширина 10 пикселей). Создаёт еду в рандомном месте карты с размером в 10 на 10 пикселей
    foodx = round(random.randrange(0, dis_width - worm_length) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - worm_length) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(background)#заполняет экран цветом заданного заднего фона и ниже обновляет статус экрана
            message("DEFEATED , R - RESTART, Q - QUIT", (204, 42, 8)) #цвет сообщения 
            Count(exact_worm_length - 1)
            pygame.display.update()
#В первом цикле "for" игра проверяет какая клавиша была нажата для продолжения действия (выход из игры -- "q" или рестарт -- "r").
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r: 
                        gameloop()# возобновляет игру если нажать "r"
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
#Во втором цикле "for" происходит движение червя на клавиши  "w", "a", "s", "d",
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: #Червь идёт влево (так как по умолчанию может только в право тут стоит минус, то есть координата отрицательная)
                    x1_change = -worm_length
                    y1_change = 0
                elif event.key == pygame.K_d: #Червь идёт вправо
                    x1_change = worm_length
                    y1_change = 0
                elif event.key == pygame.K_w: #Червь идёт вверх (тоже что и выше с правой стороной, но минус здесь у "Y" координаты)
                    y1_change = -worm_length
                    x1_change = 0
                elif event.key == pygame.K_s: #Червь идёт вниз
                    y1_change = worm_length
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #Здесь работает механика поражения, если координата тела червя столкнётся с собой в одной точке
            game_close = True

        x1 += x1_change # У головы обновляются координаты на значение "_change"
        y1 += y1_change

        dis.fill(background) # Тут интересная механика с тем, что каждый кадр обновляясь очищает предыдущий кадр
        # и рисует всё заново, а то иначе объекты будут наслаиваться.
        pygame.draw.rect(dis, meal, [foodx, foody, worm_length, worm_length]) # foodx, foody координаты еды, которые обновляются при поедании.

        worm_head = [x1, y1] #голова червя, то есть координатная точка, по которой игра ориентирует движение тела червя
        worm_list.append(worm_head) #важная строка, в которой как раз срабатывает append на worm_list расширяясь от "головы червя"
        if len(worm_list) > exact_worm_length: #если длина листа червя стала больше его текущей длины
            del worm_list[0]

        for x in worm_list[:-1]:
            if x == worm_head:
                game_close = True

        worm_eating(worm_length, worm_list)
        Count(exact_worm_length - 1)#так как червь начинается с длины 1, то это значение равно количеству съеденной еды, а значит и количеству очков.

        pygame.display.update()
#в первом "if"-e производится деление на 10 и умножение потом на 10, чтобы координаты еды совпадали с сеткой,
#по которой двигается червь (шаг и ширина 10 пикселей). Срабатывает, когда уже до этого еда была съеденна червём
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - worm_length) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - worm_length) / 10.0) * 10.0
            exact_worm_length += 1
            if worm_speed < 40: # скорость червя увеличивается вплоть до 40 на 1 единиц за каждый съёденный кусок яблока
                worm_speed += 1

        clock.tick(worm_speed)# привязывает скорость смены кадров к worm_speed, так как значение 12 у worm_speed должно оставаться неизменным, чтобы игра не обновлялась слишком быстро

    pygame.quit()#закрывает игру
    quit()

gameloop()#делает из игры цикл, если игрок не нажмёт на выход из игры ранее

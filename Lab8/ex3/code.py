# Paint

import pygame
pygame.init()  # Инициализация Pygame

screen = pygame.display.set_mode((800, 600))  # Установка размеров окна

clock = pygame.time.Clock()  # Создание объекта Clock для управления FPS

RED = (230, 0, 0)  # Цвета в формате RGB
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE]  # Список доступных цветов
color = WHITE  # Изначальный цвет - белый

eraser = pygame.image.load(r'C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab8\ex3\eraser.png')  # Загрузка изображения ластика
eraser = pygame.transform.scale(eraser, (70, 70))  # Изменение размера изображения
eraser_rect = eraser.get_rect(topleft=(1010, 0))  # Задание прямоугольной области для ластика

def draw_rect(index):
    """Функция для рисования прямоугольников выбора цвета"""
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))

def pick_color():
    """Функция для выбора цвета"""
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0 <= x <= 40 and 0 <= y <= 40:
            return RED
        elif 40 < x <= 80 and 0 <= y <= 40:
            return GREEN
        elif 80 < x <= 120 and 0 <= y <= 40:
            return BLUE
        elif 1010 <= x <= 1080 and 0 <= y <= 40:
            return BLACK
    return color

def painting(color, mode):
    """Функция для рисования с указанным цветом и режимом"""
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0] and not (0 <= x <= 400 and 0 <= y <= 90):
        if mode == 'circle':
            pygame.draw.circle(screen, color, (x, y), 27)
        elif mode == 'rect':
            pygame.draw.rect(screen, color, (x, y, 40, 40), 4)
        elif mode == 'right_triangle':
            pygame.draw.polygon(screen, color, ((x, y), (x, y+40), (x+40, y+40)), 3)
        elif mode == 'equal_triangle':
            pygame.draw.polygon(screen, color, ((x,y), (x+20, y-40), (x+40, y)))
        elif mode == 'rhomb':
            pygame.draw.polygon(screen, color, ((x, y), (x+20, y-20), (x+40, y), (x+20, y+20)))
        elif mode == 'eraser':
            pygame.draw.circle(screen, WHITE, (x, y), 20)  # Используем белый цвет для эффекта стирания

mode = 'circle'  # Изначальный режим - круг

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for i in range(len(colors)):
        draw_rect(i)  # Рисуем прямоугольники для выбора цвета

    screen.blit(eraser, (1010, 0))  # Отображаем изображение ластика
    rect = pygame.draw.rect(screen, WHITE, (130, 0, 40, 40), 3)
    circle = pygame.draw.circle(screen, WHITE, (197, 20), 23, 3)
    right = pygame.draw.polygon(screen, WHITE, ((230, 0), (230, 40), (270, 40)), 3)
    equal = pygame.draw.polygon(screen, WHITE, ((280, 40), (300, 0), (320, 40)), 3)
    rhomb = pygame.draw.polygon(screen, WHITE, ((330, 20), (350,0), (370, 20), (350, 40)), 3)

    pos = pygame.mouse.get_pos()
    if rect.collidepoint(pos):
        mode = "rect"
    if circle.collidepoint(pos):
        mode = "circle"
    if right.collidepoint(pos):
        mode = 'right_triangle'
    if equal.collidepoint(pos):
        mode = 'equal_triangle'
    if rhomb.collidepoint(pos):
        mode = 'rhomb'
    if eraser_rect.collidepoint(pos):  # Проверяем, находится ли курсор мыши над областью ластика
        mode = 'eraser'

    color = pick_color()
    painting(color, mode)  # Рисуем с учетом выбранного цвета и режима

    clock.tick(370)  # Устанавливаем FPS
    pygame.display.update()  # Обновляем экран
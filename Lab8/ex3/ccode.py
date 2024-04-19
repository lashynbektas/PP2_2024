from math import sqrt
import math
import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

finished = False

drawing = False

color = BLACK

prev,cur = None, None

#функция для каждой фигуры:
def drawRect(color, pos, width, height):  
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4) 

def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

def square(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)

def r_triangle(color, start_pos,end_pos): #на тетради рисуем график прямоугольного треугольника, и оттуда выводим формулу для 
    x1=start_pos[0]                 #самого треугольника
    x2=end_pos[0]                 
    y1=start_pos[1]
    y2=end_pos[1]
    pygame.draw.line(screen,color,start_pos,end_pos,2)
    pygame.draw.line(screen,color,(x1,y1),(x1,y2),2)
    pygame.draw.line(screen,color,(x1,y2),(x2,y2),2)


def romb(color, start_pos ,end_pos):    #для ромба формулы нету к сожалению, методом подбора +- правильную величину вычисляем
    x1=start_pos[0]
    x2=end_pos[0]
    delta=(abs(x1-x2)//2)//sqrt(3)
    y1=start_pos[1]
    y2=end_pos[1]
    pygame.draw.line(screen,color,(x1,y1),(x1-(delta),y2),2)
    pygame.draw.line(screen,color,(x1-(delta),y2),(x2-(delta),y2),2)
    pygame.draw.line(screen,color,(x1,y1),(x2,y1),2)
    pygame.draw.line(screen,color,(x2-(delta),y2),(x2,y1),2)


def e_triangle(color,start_pos,end_pos):#так же произошли трудности с правильным треугольником, +- вывел формулу и подставил  в pygame.draw.line
    x1=start_pos[0]
    x2=end_pos[0]
    y1=start_pos[1]
    y2=end_pos[1]
    pygame.draw.line(screen,color,start_pos,end_pos,2)
    deltax=abs(x2-x1)
    deltay=abs(y2-y1)
    x4=(deltax+x1)
    y4=(deltay+y1)
    
    y4+=deltax

    pygame.draw.line(screen,color,(x4,y4),end_pos,2)
    pygame.draw.line(screen,color,start_pos,(x4,y4),2)
RAD = 30


screen.fill(WHITE)
#позиции во время рисования:
start_pos = 0
end_pos = 0

#меняем фигуры и тд:
mode = 0

#массив с разными 20 цветами
all_colors = []

for _ in range(20):
    all_colors.append((randint(0,255), randint(0,255), randint(0,255)))


while not finished:

    pos = pygame.mouse.get_pos() #позиция на которой находится курсор 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #выход из программы
            finished = True
        
        #choose the color:
        if event.type == pygame.MOUSEBUTTONDOWN:#мышка была зажата
            drawing = True
            start_pos = pos# начало зажатия мышки

            if pos[0] > 20 and pos[0] < 720 and pos[1] > 20 and pos[1] < 40: #выбор цвета 
                color = screen.get_at(pos)
       
        if event.type == pygame.MOUSEBUTTONUP:#мышка была отпущена 
            drawing = False
            end_pos = pos# записываем конец нажатия мышки

            rect_x = abs(start_pos[0] - end_pos[0])#разница х
            rect_y = abs(start_pos[1] - end_pos[1])#разница у
            
            if mode == 1:                              #выбор режима
                drawRect(color, start_pos, rect_x, rect_y)
            elif mode == 3:
                drawCircle(color, start_pos, rect_x)
            elif mode==4:
                if rect_x<rect_y:rect_x=rect_y
                square(color, start_pos, rect_x, rect_x)
            elif mode==5:
                r_triangle(color, start_pos,end_pos)
            elif mode==6:
                e_triangle(color, start_pos,end_pos)
            elif mode==7:
                romb(color, start_pos,end_pos)
        if event.type == pygame.MOUSEMOTION and drawing:  #стерка 
            if mode == 2:
                eraser(pos, RAD)
        
        if event.type == pygame.MOUSEBUTTONDOWN and mode == 0:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION and mode == 0 :
            cur = pygame.mouse.get_pos()
            if prev:
                pygame.draw.line(screen, color, prev, cur, 1)
                prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
        
        if event.type == pygame.KEYDOWN:               #при нажатий на space мы будем переходить на следующий мод
            if event.key == pygame.K_SPACE:             #и если мы на 6 моде нажмем еще раз на пробел, то нас перекинет на 1 мод(0)
                mode += 1
                if mode==7:mode=0
            if event.key == pygame.K_BACKSPACE:      #при нажатия на backspace, весь экран очищается
                screen.fill(WHITE)

    w = 30  # ширина квадритиков с 20 цветами 
   
    for i, col in enumerate(all_colors):
        pygame.draw.rect(screen, col, (20 + i * w, 20, w, 20)) #цвета
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
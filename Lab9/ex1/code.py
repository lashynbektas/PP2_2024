# Racer 2.0

# Racer 2.0

# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# Установка FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Другие переменные для использования в программе
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Установка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Загрузка фонового изображения
background = pygame.image.load(r"C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab9\ex1\AnimatedStreet.jpg")

# Создание белого экрана
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Появление врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab9\ex1\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Появление монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab9\ex1\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Появление новой монеты
class Blackcoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab9\ex1\difcoin.webp")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 20), 0)  

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 20), 0)

# Управление игроком
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab9\ex1\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
         
        if self.rect.left >= 30:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right <= 370:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Установка спрайтов        
P1 = Player()
E1 = Enemy()
Coin1 = Coin()
Coin2 = Blackcoin()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Коллекция монет
coin_add = pygame.sprite.Group()
blackcoin_add = pygame.sprite.Group()

# Создание нового пользовательского события
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 100000)

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Перемещение и перерисовка всех спрайтов
    if SCORE >= 40:
        SPEED = 10
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    for entity in coin_add:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    for entity in blackcoin_add:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Обработка коллизий между игроком и врагами
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r'C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab9\ex1\crash.wav').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Коллизия с монетой
    coin_add.add(Coin1)
    if pygame.sprite.spritecollideany(P1, coin_add):
        pygame.mixer.Sound(r'C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab9\ex1\coin.wav').play()
        for entity in coin_add:
            entity.kill() 
            SCORE += 2
            Coin1 = Coin()

    # Коллизия с монетой 2
    blackcoin_add.add(Coin2)
    if pygame.sprite.spritecollideany(P1, blackcoin_add):
        pygame.mixer.Sound(r'C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab9\ex1\coin.wav').play()
        for entity in blackcoin_add:
            entity.kill() 
            SCORE += 5
            Coin2 = Blackcoin()

    pygame.display.update()
    FramePerSec.tick(FPS)
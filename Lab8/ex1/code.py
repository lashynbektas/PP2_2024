# Racer

import pygame
import random
import sys

pygame.init()

FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMY_STEP = 5  # Corrected variable name

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCORE = 0

clock = pygame.time.Clock()

score_font = pygame.font.SysFont("Verdana", 20)

SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Racer")

wasted = pygame.image.load(r'C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab8\ex1\over.jpg')
wasted = pygame.transform.scale(wasted, (400, 600))

bg = pygame.image.load(r"C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab8\ex1\AnimatedStreet.jpg")

pygame.mixer.music.load(r'C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab8\ex1\background.wav')
pygame.mixer.music.play(-1)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab8\ex1\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):  
        self.rect.move_ip(0, ENEMY_STEP)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab8\ex1\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self): 
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab8\ex1\coin.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self): 
        self.rect.move_ip(0, 5)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)
    
    def spawn(self):
        self.rect.center = (random.randint(30, 350), 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()
C1 = Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)
coin = pygame.sprite.Group()
coin.add(C1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    C1.update()
    E1.update()
    

    if pygame.sprite.spritecollideany(P1, enemies): 
        pygame.mixer.music.load(r'C:\Users\Айтас Култасов\Desktop\pp2\Practice\Lab8\ex1\crash.wav')
        pygame.mixer.music.play()

        SURF.blit(wasted, (0, 0))
        pygame.display.update()
        pygame.time.delay(3000)  
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, coin): 
        SCORE += 1
        ENEMY_STEP += 0.5
        C1.spawn()  
    
    SURF.blit(bg, (0, 0))

    E1.draw(SURF)
    C1.draw(SURF)
    P1.draw(SURF)

    score_img = score_font.render(str(SCORE), True, BLACK)
    SURF.blit(score_img, (10, 10))


    pygame.display.update()
    clock.tick(FPS)
# Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored

import pygame

white = (255, 255, 255)
red = (255, 0, 0)


x = 350  
y = 300  


pygame.init()
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()
FPS = 60


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= 20
    if keys[pygame.K_DOWN]:
        y += 20
    if keys[pygame.K_LEFT]:
        x -= 20
    if keys[pygame.K_RIGHT]:
        x += 20


    if x < 25:
        x = 25
    elif x > 675:
        x = 675
    if y < 25:
        y = 25
    elif y > 575:
        y = 575


    screen.fill(white)

    pygame.draw.circle(screen, red, (x, y), 25)

    pygame.display.flip()

pygame.quit()
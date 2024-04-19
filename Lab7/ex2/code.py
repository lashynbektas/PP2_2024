# Create music player with keyboard controller. You have to be able to press keyboard: play, stop, next and previous as some keys. Player has to react to the given command appropriately.

import pygame 

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Music Player")


image = pygame.image.load('mus.jpeg')
image = pygame.transform.scale(image, (400, 300))


music = ["Brent Faiyaz - Best Time.mp3", "Childish Gambino - 3005.mp3",
         "Frank Ocean - Lost.mp3", "wave to earth - love.mp3", "KISS OF LIFE - Nobody Knows.mp3", "Madison Beer - Home To Another One.mp3"]


current_music = 0
pygame.mixer.music.load(music[current_music])

pygame.mixer.music.play()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                current_music = (current_music + 1) % len(music)
                pygame.mixer.music.load(music[current_music])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_music = (current_music - 1) % len(music)
                pygame.mixer.music.load(music[current_music])
                pygame.mixer.music.play()


    screen.blit(image, (0, 0))
    pygame.display.flip()


pygame.quit()
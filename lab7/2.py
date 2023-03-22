import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
list = ['1.mp3', '2.mp3', '3.mp3']
t  = 0
for i in range(len(list)):
    k = i
    pygame.mixer.music.load(list[i])
    pygame.mixer.music.play(0)
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END:
            print('the song ended!')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            k -= 1
            if 0 <= k and k <= 2:
               pygame.mixer.music.load(list[k])
               pygame.mixer.music.play(0)
            elif k < 0:
                 k = 2
                 pygame.mixer.music.load(list[k])
                 pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            k += 1
            if  k >= 0 and k <= 2:
               pygame.mixer.music.load(list[k])
               pygame.mixer.music.play(0)
            elif k > 2:
                 k = 0
                 pygame.mixer.music.load(list[k])
                 pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and event.key == pygame.mixer.music.play(0):
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: 
            pygame.mixer.music.unpause()


    screen.fill((0, 255, 0))
    pygame.display.flip()

pygame.quit()
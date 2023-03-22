import sys
import pygame
from datetime import datetime
import os
def degree(k):
    k-=6
    return k
n=0
k=0
pygame.init()
W=800
H=800

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    screen=pygame.display.set_mode((W, H))
    screen.fill((250, 255, 255))

    clock2=pygame.image.load('Mikky2.png')

    gato = pygame.transform.scale(clock2,(700,500))    
    screen.blit(gato, (50,170))
   
    st=pygame.image.load('second_hand.png')
    st.set_colorkey((255,255,255))
    n=degree(n)
    pygame.time.wait(1000)
    rot = pygame.transform.rotate(st, degree(n))
    rot_rect = rot.get_rect(center=(400, 420))
    screen.blit(rot, rot_rect)



    if n%360==0:
        k-=6
    else:
        k+=0


    st2=pygame.image.load('minutes_hand.png')
    st2.set_colorkey((255,255,255))
    rot2 = pygame.transform.rotate(st2, k)
    rot_rect2 = rot2.get_rect(center=(400, 420))
    screen.blit(rot2, rot_rect2)
    pygame.display.update()
    pygame.time.delay(20)
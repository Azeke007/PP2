import random
from tabnanny import check
import pygame  
pygame.init() 
 
BLACK = (0,0,0) 
 
WHITE =(255,255,255) 
 
BLUE = (0,0,255) 
 
GREEN = (0,255,0) 
 
RED = (255,0,0) 
 
C = (100,100,100) 
 
 
rect_x = 350 
 
rect_y = 250  
rect_change_x = 2 
rect_change_y = 2 
x_food = random.randint(0,650)
y_food = random.randint(0,350)
color = WHITE 
scope = 1
speed = 2
 
size =  (700,500) 
 
right = True 
left = False 
W = False 
D = False 
snake = [] 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Zmeika") 
clock = pygame.time.Clock() #FPS 
done = False 
block = 'a'
while not done: 
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w and block!= 'w': 
            block = 's'
            right = False 
            left = False 
            W = True 
            D = False 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d and block!= 'd': 
            block = 'a'
            right = True 
            left = False 
            W = False 
            D = False 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a and block!= 'a': 
            block = 'd'
            right = False 
            left = True 
            W = False 
            D = False 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and block!= 's': 
            block = 'w'
            right = False 
            left = False 
            W = False 
            D = True 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_j: 
            scope+=1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
            if right:
               rect_change_x += speed
            if left:
                 rect_change_x += speed
            if D:
                rect_change_y += speed
            else:
               rect_change_y += speed    
    if right == True: 
        rect_x += rect_change_x 
    if left == True: 
        rect_x -= rect_change_x 
    if D == True: 
        rect_y += rect_change_y  
    if W == True: 
        rect_y -= rect_change_y 
    if rect_y>500:
        rect_y = 0
    if rect_x>700:
        rect_x = 0
    if rect_x<0:
        rect_x = 700
    if rect_y<0:
        rect_y = 500
    
    
    snake.append((rect_x,rect_y)) 
    
    screen.fill(BLACK) 
    txt = 'SCOPE:'+str(scope)     
    font = pygame.font.Font(None,50) 
    text1 = font.render(txt,True,RED) 
    screen.blit(text1,[0,0]) 
    snake = snake[-scope*2:]
    if len(snake)!=len(set(snake)):
        done = True
    for i,j in snake: 
        pygame.draw.rect(screen,GREEN,[i,j,15,15])
    pygame.draw.rect(screen,BLUE,[x_food,y_food,15,15])
    if (x_food-15 <=(snake[len(snake)-1][0] or snake[len(snake)-1][0]+15 or snake[len(snake)-1][0]-15)<=x_food+15) and (y_food - 15 <=(snake[len(snake)-1][1] or snake[len(snake)-1][1]+15 or snake[len(snake)-1][1]-15)<=y_food+15):
        scope+=1
        x_food = random.randint(0,650)
        y_food = random.randint(0,450)
    clock.tick(60)#60FPS 
    pygame.display.update() 
 
pygame.quit()
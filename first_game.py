import pygame
import sys

#initialse pygame

pygame.init()


screen_width=800
screen_height=600


screen=pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("My first game")

# create a rectangle 

rect_x=screen_width//2
rect_y=screen_height//2

rect_width=50
rect_height=50 

rect_color=(0,255,0)

player_rect=pygame.Rect(rect_x,rect_y,rect_width,rect_height)


#game loop 

while True: 
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    keys=pygame.key.get_pressed()
    
    # move the rect according to keys
    
    if keys[pygame.K_LEFT]and player_rect.left>0:
        player_rect.x-=5
    if keys[pygame.K_RIGHT] and player_rect.right<screen_width:
        player_rect.x+=5
    if keys[pygame.K_UP] and player_rect.top>0:
        player_rect.y-=5
    if keys[pygame.K_DOWN] and player_rect.bottom<screen_height:
        player_rect.y+=5
        
    # clear screen 
    
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen,rect_color,player_rect)
    
    
    #update display
    pygame.display.flip()
        
        
        
        

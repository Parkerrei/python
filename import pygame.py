import pygame
import sys

screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('images in pygame!')

pawn = pygame.image.load('D:\python folder\images\white_king.png')
pawn_rect = pawn.get_rect(topleft=(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit() 
    
    screen.fill('white')
    screen.blit(pawn,(pawn_rect))
    pygame.display.update()
    
    
# import pygame 
pygame.init() 

screen = pygame.display.set_mode((500,500))
image = pygame.image.load('D:\python folder\images\white_king.png')

screen.blit(image,(250,250))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(image,(250,250))
    pygame.display.flip()
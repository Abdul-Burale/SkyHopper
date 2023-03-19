import pygame, sys, csv

if sys.version_info < (3,5):
    print("This game requires at leasst version 3.5 of Python. Please download it from ww.python.org")
    sys.exit()

#Map
Game_Map_1 = [[0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#Initialize Pygame
pygame.init()

#Game Settings
RUN = True
Clock = pygame.time.Clock()

#Define Constants
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 750
TITLE = "Platformer"
Sprite_Width = 32
Sprite_Height = 32
Block_Width = 40
Block_Height = 40
NUM_ROWS = 4
NUM_COLUMNS = 14
GRAVITY = 0.5



#Window Creation
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(TITLE)

#Game Assets
BG_IMG = pygame.transform.scale(pygame.image.load("Asset/Background.png"), (WINDOW_WIDTH, WINDOW_HEIGHT)) 
Sprite_Sheet_Img = pygame.image.load("Asset/SpriteSheet.png").convert_alpha()




class Level(pygame.sprite.Sprite):
    pass

Sprite_List = []

for Row in range(NUM_ROWS):
    for Col in range(NUM_COLUMNS):
        x = Col * Block_Width
        y = Row * Block_Height
        Sprite_Surface = pygame.Surface((Sprite_Width, Sprite_Height))
        Sprite_Surface.blit(Sprite_Sheet_Img, (0, 0), (x , y, Sprite_Width, Sprite_Height))
        Sprite_Rect = pygame.Rect(x, y, Sprite_Width, Sprite_Height)
        
        #WINDOW.blit(Sprite_Sheet_Img, (X * 32, Y * 32), (X * 32, Y * 32, 32 , 32))
        Sprite_List.append((Sprite_Surface, Sprite_Rect))


while RUN:
    pygame.display.update()
    WINDOW.blit(BG_IMG, (0,0)) 
    
    for event in pygame.event.get():
       pygame.event.get()
       if event.type == pygame.QUIT:
           RUN = False


    
    WINDOW.blit(Sprite_List[21][0], (0, 0))
        #WINDOW.blit(Sprite_Sheet_Img, (0,0), (0,40, 32, 32))

    

import pygame, sys

if sys.version_info < (3,5):
    print("This game requires at leasst version 3.5 of Python. Please download it from ww.python.org")
    sys.exit()


#Define Constants
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 750
TITLE = "Platformer"
GRAVITY = 0.5


#Initialize Pygame
pygame.init()

#Window Creation
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(TITLE)

#Game Assets
BG_IMG = pygame.transform.scale(pygame.image.load("Asset/Background.png"), (WINDOW_WIDTH, WINDOW_HEIGHT)) 
Sprite_Sheet_Img = pygame.image.load("Asset/SpriteSheet.png")

#Game Settings
NUM_ROWS, NUM_COLUMNS = 15, 30
RUN = True
Clock = pygame.time.Clock()

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
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

class Level(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Width = 50
        self.Height = 50
        self.Tile_List = []

            
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Define Player Attributes
        self.Width = 50
        self.Height = 50
        self.image = ""
        self.rect = self.image.get_rect()                
        self.last_update = pygame.time.get_ticks()
        self.jumped = False




while RUN:
    pygame.display.update()
    WINDOW.blit(BG_IMG, (0,0)) 
    Row_Count = 0
    for Row in Game_Map_1:
        Col_Count = 0
        for Tile in Row:
           if Tile == 0:
            WINDOW.blit(Sprite_Sheet_Img, (Row_Count * 32, Col_Count * 32), (Row_Count * 40, Col_Count * 40, 32 ,32))
            Col_Count += 1
    Row_Count += 1

        
    
    

    #WINDOW.blit(Sprite_Sheet_Img, (0,0), (0,40, 32, 32))

    

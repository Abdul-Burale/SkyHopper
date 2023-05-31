import pygame, sys

#Map List - (TODO: Improve this from another file so code base is less chunky or used CSV
Game_Map_1 = [[0,0,0,20,21,23,24,25,22,47,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,2,5,5,34,1,2,15,6,3,3,0,0,0,0,1,4,4,4,4,4,4,4,4,4,4,4,4,2],
             [11,10,5,5,34,11,10,15,15,15,3,13,13,13,13,11,3,3,3,3,3,3,3,3,3,3,3,3,10],
              [5,5,5,5,31,5,5,5,5,5,5,5,5,5,26,5,5,5,5,27,5,5,5,5,5,5,5,5,5],
              [5,5,5,5,33,32,32,32,35,35,35,32,33,37,27,37,37,37,37,36,0,0,0,0,0,0,0,0,0],
              [1,4,4,4,2,6,44,44,46,47,47,47,47,47,47,47,47,47,47,47,47,47,48,51,51,53,53,1,2],
             [12,5,5,5,12,44,44,6,44,44,44,44,6,44,44,44,44,44,44,44,44,44,22,0,0,0,0,0,0],
             [12,5,5,5,12,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,22,0,0,0,0,0,0,5,5],
             [12,5,5,5,12,44,7,7,6,44,44,44,44,44,44,44,44,44,44,44,16,16,16,16,16,16,16,5,5]]

class Platformer:
    def __init__(self):
        
        #Check my python version| (TODO:
        if sys.version_info < (3, 5):
            printf("This game requires at least version 3.5 of Python!")

        # Init Pygame
        pygame.init()

        # Game States/Settings
        self.RUN = True
        self.Clock = pygame.time.Clock()

        #Define my platformer constanst
        #(TODO: Maybe get window client dimensions and then aspect it down)
        self.WINDOW_WIDTH = 1500
        self.WINDOW_HEIGHT = 750
        self.TITLE = "Platformer"

        # Block is the allocated spaces for each sprite in my spriteSheet
        self.SPRITE_WIDTH = 32
        self.SPRITE_HEIGHT = 32
        self.BLOCK_WIDTH = 40
        self.BLOCK_HEIGHT = 40
        self.NUM_ROWS = 4
        self.NUM_COLOUMS = 15

        #Window Creation
        self.WINDOW = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(self.TITLE)

        #Game Assets
        self.BG_IMG = pygame.transform.scale(pygame.image.load("Asset/Background.png"), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)) 
        self.SPRITE_SHEET_IMG = pygame.image.load("Asset/SpriteSheet.png").convert_alpha()
        self.SPRITE_LIST = self.CREATE_SPRITE_LIST()


    def CREATE_SPRITE_LIST(self):
        LIST = []
        for ROW in range(self.NUM_ROWS):
            for CELL in range(self.NUM_COLOUMS):
                X = CELL * self.BLOCK_WIDTH
                Y = ROW * self.BLOCK_HEIGHT
                
                SPRITE_SURFACE = pygame.Surface((self.SPRITE_WIDTH, self.SPRITE_HEIGHT))
                SPRITE_SURFACE.blit(self.SPRITE_SHEET_IMG, (0, 0), (X , Y, self.SPRITE_WIDTH, self.SPRITE_HEIGHT))
                SPRITE_RECT = pygame.Rect(X, Y, self.SPRITE_WIDTH, self.SPRITE_HEIGHT)

                 #Set sprite image color key transparent. (TODO: Find a better way to do this)
                SPRITE_SURFACE.set_colorkey((255, 255, 255))
                # Add all my small sprints into my sprite list - With their RECTS
                LIST.append((SPRITE_SURFACE, SPRITE_RECT))
    
        return LIST
        
    
    def update(self):
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUN = False

    def draw(self):
        self.WINDOW.blit(self.BG_IMG, (0,0))

        for row in range(len(Game_Map_1)):
            for col in range(len(Game_Map_1[row])):
                SPRITE_IDX = Game_Map_1[row][col]
                if 0 <= SPRITE_IDX < len(self.SPRITE_LIST):
                    SPRITE_SURFACE, SPRITE_RECT = self.SPRITE_LIST[SPRITE_IDX]
                    self.WINDOW.blit(SPRITE_SURFACE, (col * SPRITE_RECT.width, row * SPRITE_RECT.height))
        

     
    
P1 = Platformer()
while P1.RUN:
    P1.update()
    P1.draw()



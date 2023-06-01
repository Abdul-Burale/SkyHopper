import pygame, sys

#Map List - (TODO: Improve this from another file so code base is less chunky or used CSV

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
        self.GAME_MAP = self.LOAD_MAP('Map')

        #Window Creation
    
        self.WINDOW = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.DISPLAY = pygame.Surface((self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2))
        pygame.display.set_caption(self.TITLE)

        #Game Assets
        self.BG_IMG = pygame.transform.scale(pygame.image.load("Asset/Background.png"), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)) 
        self.SPRITE_SHEET_IMG = pygame.image.load("Asset/SpriteSheet.png").convert_alpha()
        self.SPRITE_LIST = self.CREATE_SPRITE_LIST()

    def LOAD_MAP(self, path):
        f = open(path + '.txt', 'r')
        data = f.read()
        f.close()

        data = data.split('\n')
        Game_Map = []
        for row in data:
            Converted_Row = [int(char) for char in row]
            Game_Map.append(Converted_Row)
        return Game_Map

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
        self.DISPLAY.blit(self.BG_IMG, (0, 0))

        for row in range(len(self.GAME_MAP)):
            for col in range(len(self.GAME_MAP[row])):
                SPRITE_IDX = self.GAME_MAP[row][col]
                if 0 <= SPRITE_IDX < len(self.SPRITE_LIST):
                    SPRITE_SURFACE, SPRITE_RECT = self.SPRITE_LIST[SPRITE_IDX]
                    self.DISPLAY.blit(SPRITE_SURFACE, (col * SPRITE_RECT.width, row * SPRITE_RECT.height))
        
        self.WINDOW.blit(pygame.transform.scale(self.DISPLAY, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)), (0, 0))

     
    
P1 = Platformer()
while P1.RUN:
    P1.update()
    P1.draw()



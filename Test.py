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
        self.GAME_MAP = self.LOAD_MAP('Asset/TestMap')

        #Window Creation
    
        self.WINDOW = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.DISPLAY = pygame.Surface((self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2))
        pygame.display.set_caption(self.TITLE)

        #Game Assets
        self.BG_IMG = pygame.transform.scale(pygame.image.load("Asset/Background.png"), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)) 
        self.SPRITE_SHEET_IMG = pygame.image.load("Asset/SpriteSheet.png").convert_alpha()
        self.SPRITE_LIST = self.CREATE_SPRITE_LIST()
        self.SCROLL = [0 , 0]

    def LOAD_MAP(self, path):
        f = open(path + '.txt', 'r')
        data = f.read()
        f.close()

        #\n => delimiter
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
                if SPRITE_IDX == 6:
             #    if 0 <= SPRITE_IDX < len(self.SPRITE_LIST):
                    SPRITE_SURFACE, SPRITE_RECT = self.SPRITE_LIST[SPRITE_IDX]
                    self.DISPLAY.blit(SPRITE_SURFACE, (col * SPRITE_RECT.width, row * SPRITE_RECT.height))
        Player.update()
                
        self.WINDOW.blit(pygame.transform.scale(self.DISPLAY, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)), (0  , 0))
        
        self.SCROLL[0] -= 0.1


class Player:
    def __init__(self, display):
        #Player
        self.DISPLAY = display
        self.POS_X = 0
        self.POS_Y = 0
        self.ACTION = 0
        self.FRAME = 0
        self.PLAYER_WIDTH = 50
        self.PLAYER_HEIGHT = 50
        self.POS = [self.POS_X, self.POS_Y]
        self.ACTION_LIST = []
        self.ACTION_ANI("Asset/idle/man_{}.png", 4)
        self.ACTION_ANI("Asset/run/man_{}.png", 6)


        #Deal with player state animations. (TODO: As gamne gets more complicated come back to update thsi()
        self.PLAYER_IMAGE = self.ACTION_LIST[self.ACTION][self.FRAME]
        
        self.VELOCITY_X = 0
        self.VELOCITY_Y = 0
        self.ACCELERATION_X = 0
        self.ACCELERATION_Y = 0
        self.GRAVITY = 0.5
        self.JUMPING = False;
        self.FALLING = False;
        self.LAST_UPDATE = pygame.time.get_ticks()
        #init animations

    def ACTION_ANI(self, PATH, RANGE):
        Temp_List = []
        for i in range(RANGE):
            Image_Path = PATH.format(i)
            Action_Image = pygame.image.load(Image_Path).convert()
            Action_Image.set_colorkey((255, 255, 255))
            Temp_List.append(Action_Image)
        self.ACTION_LIST.append(Temp_List)
    
    def update(self):
        global LAST_UPDATE
        self.PLAYER_IMAGE = self.ACTION_LIST[self.ACTION][self.FRAME]
        
        KEY = pygame.key.get_pressed()
        if KEY[pygame.K_1]:
            self.ACTION = 0

        if KEY[pygame.K_2]:
            self.ACTION = 1

        CURRENT_TIME = pygame.time.get_ticks()
        if CURRENT_TIME - self.LAST_UPDATE >= 250:
            self.FRAME += 1
            self.LAST_UPDATE = CURRENT_TIME
            if self.ACTION_LIST[0]:
                if self.FRAME >= 4:
                    self.FRAME = 0

            elif self.ACTION_LIST[1]:
                if self.FRAME >= 6:
                    self.FRAME = 0

        

        self.DISPLAY.blit(self.PLAYER_IMAGE, (self.POS[0], self.POS[1]))

P1 = Platformer()
Player = Player(P1.DISPLAY)
while P1.RUN:
    P1.update()
    P1.draw()
    Player.update()



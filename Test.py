import pygame, sys


class Platformer:
    def __init__(self):
        
        if sys.version_info < (3, 5):
            raise Exception("This game requires at least version 3.5 of Python!")

        # Init Pygame
        pygame.init()

        # Game States/Settings
        self.RUN = True
        self.Clock = pygame.time.Clock()

        # Player details
        self.PLAYER = None

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

        self.GAME_PADDING = 352
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
    
    #TODO: Take this player argument and wrap it in a functiont aht sets all arguments passed from other classess.
    def update(self, player):
        self.PLAYER = player
        pygame.display.update()
        self.Handle_Input()
        self.Check_Collision()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUN = False
        

        self.SCROLL[0] += (player.POS_X - self.SCROLL[0] -  self.GAME_PADDING)
        self.draw()
    
    def draw(self):

        if Player.POS_X < 350:
            self.DISPLAY.blit(self.BG_IMG, ( 0, 0))
        else:
            self.DISPLAY.blit(self.BG_IMG, (-self.SCROLL[0], 0))

        for row in range(len(self.GAME_MAP)):
            for col in range(len(self.GAME_MAP[row])):
                SPRITE_IDX = self.GAME_MAP[row][col]
                if SPRITE_IDX == 6:
                 
                    if 0 <= SPRITE_IDX < len(self.SPRITE_LIST):
                        SPRITE_SURFACE, SPRITE_RECT = self.SPRITE_LIST[SPRITE_IDX]
                        SPRITE_RECT.x = (col * SPRITE_RECT.width)
                        SPRITE_RECT.y = (row * SPRITE_RECT.height)
                        
                        
                        if Player.POS_X < 350:
                        # Camera stops moving as player is near the Wall
                            self.DISPLAY.blit(SPRITE_SURFACE, (SPRITE_RECT))
                            pygame.draw.rect(self.DISPLAY, (255, 255, 255), SPRITE_RECT, width=1)
                        else:
                            self.DISPLAY.blit(SPRITE_SURFACE, ((SPRITE_RECT.x  - self.SCROLL[0]) , SPRITE_RECT.y))
                            #pygame.draw.rect(self.DISPLAY, (255, 255, 255), (SPRITE_RECT.x - self.SCROLL[0], SPRITE_RECT.y, 50 / 1.5, 50 / 1.5), width=1)


        
        Player.Update(P1)

        if self.PLAYER.PLAYER_RECT.x < 350:
            pygame.draw.rect(self.DISPLAY, (255, 255, 255), self.PLAYER.PLAYER_RECT, width=1)
        else:
            pygame.draw.rect(self.DISPLAY, (255, 255, 255), (self.PLAYER.PLAYER_RECT.x - self.SCROLL[0], self.PLAYER.PLAYER_RECT.y, self.PLAYER.PLAYER_RECT.width, self.PLAYER.PLAYER_RECT.height), width=1)

        #
        self.WINDOW.blit(pygame.transform.scale(self.DISPLAY, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT )), (0, 0))
    

    def Handle_Input(self):
       KEY = pygame.key.get_pressed()
    
       if KEY[pygame.K_ESCAPE]:
           self.RUN = False



    def Check_Collision(self):
        player_rect = self.PLAYER.PLAYER_RECT
    
        for row in range(len(self.GAME_MAP)):
            for col in range(len(self.GAME_MAP[row])):
                sprite_idx = self.GAME_MAP[row][col]
                if sprite_idx == 6:
                    sprite_rect = pygame.Rect(col * self.SPRITE_WIDTH, row * self.SPRITE_HEIGHT, self.SPRITE_WIDTH, self.SPRITE_HEIGHT)
                    if player_rect.colliderect(sprite_rect):
                        # Perform collision handling actions
                        # For example, you can update the player's position or trigger an event
                        self.PLAYER.Update_Player_Pos()
                        print("Collision")
                        return
        
class Player:
    def __init__(self, display):
        #Player
        self.DISPLAY = display
        self.POS_X = 80
        self.POS_Y = 280
        self.ACTION = 0
        self.FRAME = 0
        self.PLAYER_WIDTH = 50
        self.PLAYER_HEIGHT = 50
        self.ACTION_LIST = []
        self.ACTION_ANI("Asset/idle/man_{}.png", 4)
        self.ACTION_ANI("Asset/run/man_{}.png",6)


        #Deal with player state animations. (TODO: As gamne gets more complicated come back to update thsi()
        self.PLAYER_IMAGE = self.ACTION_LIST[self.ACTION][self.FRAME]
        self.PLAYER_RECT = pygame.Rect(self.POS_X, self.POS_Y, self.PLAYER_WIDTH // 1.5, self.PLAYER_HEIGHT // 1.5)
        
        self.DELTA_X = 0
        self.DELTA_Y = 0
        self.GRAVITY = 0

        # Direction (TODO: Will have to change this when dealing with velocity direction)
        self.JUMPING = False;
        self.FALLING = False;
        self.MOVING_RIGHT = False
        self.MOVING_LEFT = False
        self.FLIPPED = False

        # Player time  (TODO): Wrapping this globally might be bad so sort time in Platform class later
        self.LAST_UPDATE = pygame.time.get_ticks()

    def ACTION_ANI(self, PATH, RANGE):
        Temp_List = []
        for i in range(RANGE):
            Image_Path = PATH.format(i)
            Action_Image = pygame.image.load(Image_Path).convert()
            Action_Image.set_colorkey((255, 255, 255))
            Temp_List.append(Action_Image)
        self.ACTION_LIST.append(Temp_List)
    
    def Update(self, platformer):
        
        #TODO: TIDY UP
        self.PLATFORMER = platformer
        self.PLAYER_IMAGE = self.ACTION_LIST[self.ACTION][self.FRAME]  


        # Calculate time in miliseconds
        CURRENT_TIME = pygame.time.get_ticks()
        TIME_ELAPSED = CURRENT_TIME - self.LAST_UPDATE

        if TIME_ELAPSED >= 150:
            self.FRAME += 1
            self.LAST_UPDATE = CURRENT_TIME
            if self.ACTION == 0:
                if self.FRAME >= 4:
                    self.FRAME = 0
            
            if self.ACTION == 1:
                if self.FRAME >= 6:
                    self.FRAME = 0

        self.Update_Player()
        #- self.PLATFORMER.SCROLL[0]
        if self.POS_X < 350:
            self.DISPLAY.blit(pygame.transform.flip(self.PLAYER_IMAGE, self.FLIPPED, False), (self.POS_X , self.POS_Y))
        else:
            self.DISPLAY.blit(pygame.transform.flip(self.PLAYER_IMAGE, self.FLIPPED, False), (self.POS_X - self.PLATFORMER.SCROLL[0], self.POS_Y))
        



    def Update_Player(self):

        self.Handle_Input()
        self.Handle_Movement()

        #Update Delta

        # Update Player Rect Coo-ords
        self.PLAYER_RECT.x = self.POS_X
        self.PLAYER_RECT.y = self.POS_Y
        

    def Handle_Input(self):
        KEY = pygame.key.get_pressed()

        if KEY[pygame.K_a]:
            self.MOVING_LEFT = True
        else:
            self.MOVING_LEFT = False
        
        if KEY[pygame.K_d]:
            self.MOVING_RIGHT = True
        else:
            self.MOVING_RIGHT = False
        
        if KEY[pygame.K_SPACE]:
            self.JUMPED = True

        #TODO: change this later to deal with collisions to gain an extra jump
        if not KEY[pygame.K_SPACE]:
            self.JUMPED = False
            self.POS_Y += 0.005

        if not KEY[pygame.K_a] and not KEY[pygame.K_d]:
            self.ACTION = 0
            if self.ACTION == 0:
                if self.FRAME >= 4:
                    self.FRAME = 0
            else:
                self.FRAME += 1

    def Handle_Movement(self):

        # Need to change movement into Delta X & Y for collision checking
        if self.MOVING_LEFT == True and self.POS_X > -5:
            self.ACTION = 1
            self.FLIPPED = True
            self.DELTA_X -= 0.2

        if self.MOVING_RIGHT == True and self.POS_X < 1500 :
            self.ACTION = 1
            self.DELTA_X += 0.2
            self.FLIPPED = False

        if self.JUMPED == True:
            self.POS_Y -= 0.25
        
        if self.JUMPED == False:
            pass
            #self.POS[1] -= self.GRAVITY
            
        self.POS_X += self.DELTA_X
        self.POS_Y += self.DELTA_Y

        # Reset Delta values
        self.DELTA_X = 0
        self.DELTA_Y = 0

    def Update_Player_Pos(self):
        self.DELTA_X = 0
P1 = Platformer()
Player = Player(P1.DISPLAY)

while P1.RUN:
    P1.update(Player)
    P1.draw()
    Player.Update(P1)


    


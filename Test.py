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
        self.NUM_ROWS = 5
        self.NUM_COLOUMS = 15
        self.GAME_MAP = self.LOAD_MAP('Asset/TestMap')

        #Window Creation
    
        self.WINDOW = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.DISPLAY = pygame.Surface((self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2))
        pygame.display.set_caption(self.TITLE)

        #Game Assets
        self.BG_IMG = pygame.transform.scale(pygame.image.load("Asset/Background.png"), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)) 
        self.SPRITE_SHEET_IMG = pygame.image.load("Asset/SpriteSheet2.png").convert_alpha()
        self.SPRITE_LIST = self.CREATE_SPRITE_LIST()

        self.GAME_PADDING = 352
        self.SCROLL = [0 , 0]
        self.SHOW = False
        self.TILE_LIST = []

        self.CollideList = []

    def LOAD_MAP(self, path):
        f = open(path + '.txt', 'r')
        data = f.read()
        f.close()

        #\n => delimiter
        data = data.split('\n')
        Game_Map = []
        for row in data:
            Converted_Row = []
            for num_str in row.split(','):
                if num_str.isdigit():
                    Converted_Row.append(int(num_str))
            if Converted_Row:
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
    
    #TODO: Havnn't impleted this because I still want to avoid writing a huge switch statement
    def HANDLE_SPRITE_IMAGE(self, S_IDX, ROW, CELL):
        if 0 <= S_IDX < len(self.SPRITE_LIST):

            SPRITE_SURFACE, SPRITE_RECT = self.SPRITE_LIST[S_IDX]
            SPRITE_RECT.x = (CELL * SPRITE_RECT.width)
            SPRITE_RECT.y = (ROW * SPRITE_RECT.height)
        pass
    
    def update(self, player):
        self.PLAYER = player
        pygame.display.update()
        self.Handle_Input()
        #self.Check_Collision()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUN = False
        
        # Scrolling X Axis
        if Player.POS_X < 350:
            self.SCROLL[0] = 0
        elif Player.POS_X >= 1100:
            self.SCROLL[0] = 750

        else:
            self.SCROLL[0] += (self.PLAYER.POS_X - self.SCROLL[0] -  self.GAME_PADDING)

        #Scrolling On Y Axis
        if (self.PLAYER.POS_Y <= 175):
            self.SCROLL[1] = 0
        elif (self.PLAYER.POS_Y >= 550):
            self.SCROLL[1] = 375
        else:
            self.SCROLL[1] += (self.PLAYER.POS_Y - self.SCROLL[1] - 175)
        self.draw()
        
        #print("Player POS_X ==> {} self.SCROLL[0] {}".format(self.PLAYER.POS_X, self.SCROLL[0]))
    def draw(self):

        self.DISPLAY.blit(self.BG_IMG, (0 - self.SCROLL[0], 0 - self.SCROLL[1]))

        

        for row in range(len(self.GAME_MAP)):
            for col in range(len(self.GAME_MAP[row])):
                SPRITE_IDX = self.GAME_MAP[row][col]
                #TODO: Create a function that deals wiuth this
                
                if SPRITE_IDX == 0:
                    continue
            
             
                if 0 <= SPRITE_IDX < len(self.SPRITE_LIST):
                    SPRITE_SURFACE, SPRITE_RECT = self.SPRITE_LIST[SPRITE_IDX]
                    SPRITE_RECT.x = (col * SPRITE_RECT.width)
                    SPRITE_RECT.y = (row * SPRITE_RECT.height)
                    self.TILE_LIST.append(SPRITE_RECT)

                    
                    
                    if Player.POS_X < 350:
                    # Camera stops moving as player is near the Wall
                        self.DISPLAY.blit(SPRITE_SURFACE, (SPRITE_RECT.x, (SPRITE_RECT.y - self.SCROLL[1])))
                        if self.SHOW == True:
                            pygame.draw.rect(self.DISPLAY, (255, 255, 255), (SPRITE_RECT.x, SPRITE_RECT.y - self.SCROLL[1], 50 / 1.5, 50 / 1.5), width=1)
                    else:
                        self.DISPLAY.blit(SPRITE_SURFACE, ((SPRITE_RECT.x  - self.SCROLL[0]) , (SPRITE_RECT.y - self.SCROLL[1])))
                        if self.SHOW == True:
                            pygame.draw.rect(self.DISPLAY, (255, 255, 255), (SPRITE_RECT.x - self.SCROLL[0], SPRITE_RECT.y - self.SCROLL[1], 50 / 1.5, 50 / 1.5), width=1)
        
        for I in Entity_List:
           I.Update()
        
        self.PLAYER.Update(self)
        self.WINDOW.blit(pygame.transform.scale(self.DISPLAY, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT )), (0, 0))

    # Render text to screen
    def DrawMessage(self, Sentence, X, Y, font_type, display):
        pass
    

    def Handle_Input(self):
       KEY = pygame.key.get_pressed()
    
       if KEY[pygame.K_ESCAPE]:
           self.RUN = False

       if KEY[pygame.K_1]:
           self.SHOW = True
        
       if KEY[pygame.K_2]:
           self.SHOW = False
           E1.ACTION = 1
           if E1.ACTION >= 4:
               E1.ACTION = 0
           
       if KEY[pygame.K_3]:
           self.PLAYER.POS_X = 70
           self.PLAYER.POS_Y = 70
  
       if KEY[pygame.K_4]:
           self.PLAYER.POS_X = 1110
           self.PLAYER.POS_Y = 70 
       
       if KEY[pygame.K_5]:
           self.PLAYER.POS_X = 60
           self.PLAYER.POS_Y = 550
       
       if KEY[pygame.K_6]:
           self.PLAYER.POS_X = 1090
           self.PLAYER.POS_Y = 450

class Player:
    def __init__(self, display):
        #Player
        self.DISPLAY = display
        self.POS_X = 60
        self.POS_Y = 70
        self.ACTION = 0
        self.FRAME = 0
        self.PLAYER_WIDTH = 50
        self.PLAYER_HEIGHT = 50
        self.ACTION_LIST = []
        self.ACTION_ANI("Asset/idle/man_{}.png", 4)
        self.ACTION_ANI("Asset/run/man_{}.png",6)
        self.HEALTH = 100
        self.HEALTH_RECT = pygame.Rect(self.POS_X, self.POS_Y, 35, 5)

        #Deal with player state animations. (TODO: As gamne gets more complicated come back to update thsi()
        self.PLAYER_IMAGE = self.ACTION_LIST[self.ACTION][self.FRAME]
        self.PLAYER_RECT = pygame.Rect(self.POS_X, self.POS_Y, self.PLAYER_WIDTH // 2, self.PLAYER_HEIGHT // 1.5)
        
        self.DELTA_X = 0
        self.DELTA_Y = 0
        self.VEL_Y = 0
        self.GRAVITY = 0.007

        # Direction (TODO: Will have to change this when dealing with velocity direction)
        self.JUMPED = False
        self.FALLING = False
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
        pygame.draw.rect(self.DISPLAY, (0, 255, 0), self.HEALTH_RECT)



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
        
        if self.POS_X < 350:
            self.DISPLAY.blit(pygame.transform.flip(self.PLAYER_IMAGE, self.FLIPPED, False), (self.POS_X , self.POS_Y - self.PLATFORMER.SCROLL[1]))
        else:
            self.DISPLAY.blit(pygame.transform.flip(self.PLAYER_IMAGE, self.FLIPPED, False), (self.POS_X - self.PLATFORMER.SCROLL[0], self.POS_Y - self.PLATFORMER.SCROLL[1]))
        



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

        # Python won't let me handle jump with two different methods
        if KEY[pygame.K_SPACE] and not self.JUMPED:
            self.VEL_Y = -0.85
            self.JUMPED = True
            

        #TODO: change this later to deal with collisions to gain an extra jump
        if not KEY[pygame.K_SPACE]:
            self.FALLING = True
            if self.VEL_Y == 0:
                self.JUMPED = False
        
        #TODO: MOVE EXCAPE KEY INTO HERE
        if KEY[pygame.K_v]:
            self.HEALTH -= 1
            if (self.HEALTH <= 0):
                self.HEALTH = 100

        if not KEY[pygame.K_a] and not KEY[pygame.K_d]:
            self.ACTION = 0
            if self.ACTION == 0:
                if self.FRAME >= 4:
                    self.FRAME = 0
            else:
                self.FRAME += 1

    def Handle_Movement(self):
        # Reset Delta values
        self.DELTA_X = 0
        self.DELTA_Y = 0

    
        # Need to change movement into Delta X & Y for collision checking
        if self.MOVING_LEFT == True and self.PLAYER_RECT.x >= -5:
            self.ACTION = 1
            self.FLIPPED = True
            self.DELTA_X -= 0.75

        if self.MOVING_RIGHT == True and self.POS_X < 1477 :
            self.ACTION = 1
            self.DELTA_X += 0.75
            self.FLIPPED = False

        #Apply Gravity
        if self.FALLING == True:
            self.VEL_Y += self.GRAVITY
            if self.VEL_Y >= 0.9:
                self.VEL_Y = 0.85

        self.DELTA_Y += self.VEL_Y

        
        self.Check_Tile_Collision(self.PLATFORMER.GAME_MAP)

        
        self.POS_X += self.DELTA_X
        self.POS_Y += self.DELTA_Y 
        
        #Updating Health Rect Position Etc
        self.HEALTH_RECT.x = self.POS_X - self.PLATFORMER.SCROLL[0]
        self.HEALTH_RECT.y = (self.POS_Y - 10) - self.PLATFORMER.SCROLL[1]
        self.HEALTH_RECT.width = self.HEALTH // 3
        

    #TODO: Wrap this in a function that doesn't use a nested loop -- A little inefficient
    def Check_Tile_Collision(self, Data):
        P_RECT_DEBUG = pygame.Rect((self.PLAYER_RECT.x + self.DELTA_X) - self.PLATFORMER.SCROLL[0], (self.PLAYER_RECT.y + self.DELTA_Y) - self.PLATFORMER.SCROLL[1], self.PLAYER_RECT.width, self.PLAYER_RECT.height)
        
        for ROW in range(len(Data)):
            for CELL in range(len(Data[ROW])):
                SPRITE_IDX = Data[ROW][CELL]
                if SPRITE_IDX == 0:
                    continue

                if 30 <= SPRITE_IDX <= 75:
                    continue



                
                SPRITE_RECT = pygame.Rect(CELL * self.PLATFORMER.SPRITE_WIDTH, ROW * self.PLATFORMER.SPRITE_HEIGHT, self.PLATFORMER.SPRITE_WIDTH, self.PLATFORMER.SPRITE_HEIGHT)
                

                x_collision = False
                y_collision = False

                #X - AXIS COLLISION
                if SPRITE_RECT.colliderect(self.PLAYER_RECT.x + self.DELTA_X, self.PLAYER_RECT.y, self.PLAYER_RECT.width, self.PLAYER_RECT.height - 1):
                    x_collision = True
                    if self.PLATFORMER.SHOW == True:
                        pygame.draw.rect(self.DISPLAY, (255, 0, 0), P_RECT_DEBUG, width=1)
                        pygame.draw.rect(self.DISPLAY, (0, 255, 0), self.HEALTH_RECT)



                #Y - AXIS COLLISION
                if SPRITE_RECT.colliderect(self.PLAYER_RECT.x, self.PLAYER_RECT.y + self.DELTA_Y, self.PLAYER_RECT.width - 2, self.PLAYER_RECT.height):
                    y_collision = True
                    if self.PLATFORMER.SHOW == True:
                        pygame.draw.rect(self.DISPLAY, (255, 255, 0), P_RECT_DEBUG, width=1)

                if x_collision and y_collision:
                    # Collision on both X and Y axes
                    # Handle the collision here
                    # You can choose to adjust the player's position or apply different behavior

                    # Example: Adjust the player's position to the previous valid position
                    self.PLAYER_RECT.x -= self.DELTA_X
                    self.PLAYER_RECT.y -= self.DELTA_Y

                    # Reset the player's movement
                    self.DELTA_X = 0
                    self.DELTA_Y = 0
                    self.VEL_Y = 0

                elif x_collision:
                    # Collision on the X-axis only
                    self.PLAYER_RECT.x -= self.DELTA_X
                    self.DELTA_X = 0

                elif y_collision:
                    # Collision on the Y-axis only
                    self.PLAYER_RECT.y -= self.DELTA_Y
                    self.DELTA_Y = 0
                    self.VEL_Y = 0




class Entity:
    def __init__(self, Pos_X, Pos_Y):
        self.POZ_X = Pos_X
        self.POZ_Y = Pos_Y
        self.HEALTH = 100
        self.ACTION = 0
        self.FRAME = 0
        self.E_WIDTH = 50
        self.E_HEIGHT = 50
        self.GRAVITY = 0.005
        self.VEL_Y = 0
        self.DELTA_X = 0
        self.DELTA_Y = 0
        self.Direction = 0.5
        
        #Flags
        self.Flipped = False

        self.ACTION_LIST = []
        self.ACTION_ANI("Asset/E/idle/e_{}.png", 4)
        self.ACTION_ANI("Asset/E/walk/e_{}.png", 7)
        self.ACTION_ANI("Asset/E/attack/e_{}.png", 6)
        self.ACTION_ANI("Asset/E/death/e_{}.png", 5)
        
        self.E_IMAGE = self.ACTION_LIST[self.ACTION][self.FRAME]
        self.E_RECT = pygame.Rect(self.POZ_X, self.POZ_Y, self.E_WIDTH // 2, self.E_HEIGHT // 1.5)
        self.HEALTH_RECT = pygame.Rect(self.POZ_X, self.POZ_Y, 35, 5)

        self.LAST_UPDATE = pygame.time.get_ticks()

        #PLATFORMER
        self.PLATFORMER = P1
        self.DISPLAY = self.PLATFORMER.DISPLAY

    def Auto(self):
        self.ACTION = 1
        self.DELTA_X = self.Direction

        if self.POZ_X >= 1470:
            self.Direction = -0.5     

    
    def ACTION_ANI(self, PATH, RANGE):
        Temp_List = []
        for i in range(RANGE):
            Image_Path = PATH.format(i)
            Action_Image = pygame.image.load(Image_Path).convert()
            Action_Image.set_colorkey((255, 255, 255))
            Temp_List.append(Action_Image)
        
        self.ACTION_LIST.append(Temp_List)
    
    def Update(self):
        
        self.E_RECT.x = self.POZ_X
        self.E_RECT.y = self.POZ_Y
        
        self.E_IMAGE = self.ACTION_LIST[self.ACTION][self.FRAME]
        
        CURRENT_TIME = pygame.time.get_ticks()
        TIME_ELAPSED = CURRENT_TIME - self.LAST_UPDATE


        #APPLY A Const Gravity to Entity]
        self.VEL_Y += self.GRAVITY
        if self.VEL_Y >= 0.9:
            self.VEL_Y = 0.85

        if TIME_ELAPSED >= 150:
            self.FRAME += 1
            self.LAST_UPDATE = CURRENT_TIME
        
            #TODO: Figure how I Handle Actions
            if self.ACTION == 0:
                if self.FRAME >= 4:
                    self.FRAME = 0
            
            if self.ACTION == 1:
                if self.FRAME >= 7:
                    self.FRAME = 0
                    self.E_RECT.x += 10


            if self.ACTION == 2:
                if self.FRAME >= 6:
                    self.FRAME = 0

            if self.ACTION == 3:
                if self.FRAME >= 5:
                    self.FRAME = 4
        
        self.DELTA_Y += self.VEL_Y
        self.Auto()

        self.Check_Tile_Collision(P1.GAME_MAP)
        self.POZ_X += self.DELTA_X
        self.POZ_Y += self.DELTA_Y
        #pygame.draw.rect(self.DISPLAY, (255, 255, 255), self.E_RECT, width=1)

        # Do the Enemie Movement Loop here


        self.DISPLAY.blit(self.E_IMAGE, (self.POZ_X - self.PLATFORMER.SCROLL[0],self.POZ_Y - self.PLATFORMER.SCROLL[1]))

    def Check_Tile_Collision(self, Data):
        for Row in range(len(Data)):
            for Cell in range(len(Data[Row])):
                Tile_IDX = Data[Row][Cell]

                if Tile_IDX == 0:
                    continue

                if 30 <= Tile_IDX <= 75:
                    continue

                
                # Recalculating the X and Y of the Tiles is inefficient
                Tile_Rect = pygame.Rect(Cell * self.PLATFORMER.SPRITE_WIDTH, Row * self.PLATFORMER.SPRITE_HEIGHT, self.PLATFORMER.SPRITE_WIDTH, self.PLATFORMER.SPRITE_HEIGHT)

                #Collision Flags
                X_Collision = False
                Y_Collision = False

                if Tile_Rect.colliderect(self.E_RECT.x + self.DELTA_X, self.E_RECT.y, self.E_RECT.width, self.E_RECT.height - 1):
                    X_Collision = True

                
                if Tile_Rect.colliderect(self.E_RECT.x , self.E_RECT.y + self.DELTA_Y, self.E_RECT.width - 2, self.E_RECT.height):
                    Y_Collision = True

                if X_Collision and Y_Collision:
                    self.E_RECT.x -= self.DELTA_X
                    self.E_RECT.y -= self.DELTA_Y

                    self.DELTA_X = 0
                    self.DELTA_Y = 0
                    self.VEL_Y = 0

                elif X_Collision:
                    self.E_RECT.x -= self.DELTA_X
                    self.DELTA_X = 0

                elif Y_Collision:
                    self.E_RECT.y -= self.DELTA_Y
                    self.DELTA_Y = 0
                    self.VEL_Y = 0 
         
Entity_List = []
P1 = Platformer()
Player = Player(P1.DISPLAY)
E1 = Entity(110, 110)
E2 = Entity(160, 110)
E3 = Entity(200, 110)

#Entity_List.append(E1)
#Entity_List.append(E2)
#Entity_List.append(E3)



while P1.RUN:
    P1.update(Player)
    P1.draw()

   
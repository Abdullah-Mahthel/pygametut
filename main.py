
import pygame 

pygame.init()
################## GLOBAL VARIABLES  ###########################
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = int (SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode ((SCREEN_HEIGHT , SCREEN_HEIGHT))

moving_left = False
moving_right = False
#set Time for framerate
clock = pygame.time.Clock()
FPS = 60
#Define Colors :
BG = (144,201,120)





def draw_bg ():
            screen.fill(BG)

pygame.display.set_caption ('Shooter')
##################  CLASSES  ########################
class Soldier (pygame.sprite.Sprite):
       def __init__(self,char_type , x, y , scale , speed ):
           pygame.sprite.Sprite.__init__(self)
           self.char_type = char_type  
           self.speed = speed 
           self.direction = 1
           self.flip = False 
           
           img = pygame.image.load(f'img/{self.char_type}/Idle/0.png')
           #Enlarge image size
           #def load(filename: FileArg, namehint: str = "") -> Surface
           self.image = pygame.transform.scale(img , (int(img.get_width() * scale),int ( img.get_height()* scale)))
            #--------------------------------------- (surface - size - destination size (optional))
           # save the picture in a rectangle
           self.rect= self.image.get_rect()
           #rectangle position saved in (x and y)
           self.rect.center = (x,y)


       # a method to move player 
       def moveplayer (self , moving_left , moving_right):
           #reset movement variable Delta x and Delta y
           dx = 0
           dy = 0
           #asssign movement variables if moving_left or moving_right
           if moving_left:
               dx -=self.speed
               self.direction = -1
               self.flip = True
           if moving_right:   
               dx+= self.speed 
               self.direction = 1
               self.flip = False
           #update rectangle position 
           self.rect.x += dx
           self.rect.y += dy
           

            #How to flip an image 
           #def flip(   surface: Surface,flip_x: bool | ,flip_y: bool) 
       def draw (self):
           screen.blit(pygame.transform.flip(self.image ,self.flip,False), self.rect)
   # def blit( self,source: Surface,dest: Union[Coordinate, RectValue],area: Optional[RectValue] = None,special_flags: int = 0) -> Rect: ...
player = Soldier('player' ,200, 200 ,3 ,5) 
enemy = Soldier('enemy' ,400, 200 ,3 ,5) 



###################### GAME LOOP ################################
run = True 

while run :

       clock.tick(FPS)
       draw_bg()
       player.draw()
       enemy.draw()
       player.moveplayer(moving_left , moving_right)
      ###########  DRAWING  ###################
      #simply Quit the game
       for event in pygame.event.get():
           if event.type == pygame.QUIT :
                     run = False
           #Keyboard Handler (Press Keys)
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_a:
                   moving_left = True
                             
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_d:
                   moving_right = True 
               if event.key == pygame.K_ESCAPE:
                   run = False 
           #keyboard buttons released         
           if event.type == pygame.KEYUP:
               if event.key == pygame.K_a:
                   moving_left = False
           if event.type == pygame.KEYUP:
               if event.key == pygame.K_d:
                   moving_right = False
                             
       pygame.display.update()

pygame.quit()                 

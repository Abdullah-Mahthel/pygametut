
import pygame 
import os

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

#Define Gravity
GRAVITY = 0.75

#Define Colors :
BG = (144,201,120)

RED = (255,0,0)





def draw_bg ():
            screen.fill(BG)
            pygame.draw.line(screen,RED,(0,300) , (SCREEN_WIDTH , 300))

pygame.display.set_caption ('Shooter')
##################  CLASSES  ########################
class Soldier (pygame.sprite.Sprite):
       def __init__(self,char_type , x, y , scale , speed ):
           pygame.sprite.Sprite.__init__(self)
           self.alive = True 
           self.char_type = char_type  
           self.speed = speed 
           self.direction = 1
           self.vel_y = 0
           self.jump = False
           self.in_air = True
           self.flip = False
           #WE need to make empty list(array) to loop through all animations
           self.animation_list = [] 
           # default value of index list is zero 
           self.frame_index = 0
           # self.action means the character has many actions like idle ,run , jump and die
           self.action = 0
           # update time to know how many time run since creating the object
           self.update_time = pygame.time.get_ticks()

           # Load all images for the player by making an array of different animation action :note name of actions = file name
           animation_types = [ 'Idle' , 'Run', 'Jump']
           for animation in animation_types :
                 #temprerly list to store animation
                 temp_list = []
                 #count number of files in each folder
                 num_of_frames =len( os.listdir(f'img/{self.char_type}/{animation}'))
                 #loop through images using i 
                 for i in range(num_of_frames):
                     img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png')
                     #Enlarge image size
                     #def load(filename: FileArg, namehint: str = "") -> Surface
                     img= pygame.transform.scale(img , (int(img.get_width() * scale),int ( img.get_height()* scale)))
                     #--------------------------------------- (surface - size - destination size (optional))
                     temp_list.append(img)
                 self.animation_list.append(temp_list)    

           self.animation_list.append(temp_list)    
           
           self.image = self.animation_list [self.action][self.frame_index]    
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
           #jump 
           if self.jump == True and self.in_air == False:
               self.vel_y =-11
               self.jump = False
               self.in_air =True 
           # apply gravity
           self.vel_y += GRAVITY
           if self.vel_y > 10:
               self.vel_y
           dy += self.vel_y

           #check collision with floor
           if self.rect.bottom + dy > 300:
               dy = 300 - self.rect.bottom
               self.in_air -False 
            
               
           #update rectangle position 
           self.rect.x += dx
           self.rect.y += dy

       def update_animation (self):
           # animation timer (cool down animation) a time to flip to the next animation
           ANIMATION_COOLDOWN =100
           #update image depending on the current frame
           self.image = self.animation_list [self.action][self.frame_index]
           if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN :
               self.update_time = pygame.time.get_ticks()              
               self.frame_index +=1
           #if animation run out of images then reset back to the start of the first image
           if self.frame_index >= len(self.animation_list[self.action] ):
               self.frame_index = 0        




       def update_action (self , new_action):
           #check if the new action is different from the previous one
           if new_action != self.action :
               self.action = new_action
               #update the animation setting
               self.frame_index = 0
               self.update_time = pygame.time.get_ticks()




           

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
       player.update_animation()
       player.draw()
       enemy.draw()
       #Update player actions
       if player.alive :
          if player.in_air :
              player.update_action(2) # Jump 
          elif moving_left or moving_right :
              player.update_action(1) # which is Run

          else:
              player.update_action(0)# which is idle    
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
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE and player.alive:
                   player.jump = True

                    
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

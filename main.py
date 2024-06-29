 #استدعاء مكتبة باي قيم 
import pygame 
# تفعيل المكتبة 
pygame.init()
################## GLOBAL VARIABLES  ###########################
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = int (SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode ((SCREEN_HEIGHT , SCREEN_HEIGHT))

pygame.display.set_caption ('Shooter')
##################  CLASSES  ########################
class Soldier (pygame.sprite.Sprite):
       def __init__(self, x, y , scale ):
           pygame.sprite.Sprite.__init__(self) 
           img = pygame.image.load('img/player/Idle/0.png')
           # تكبير حجم الصورة
           self.image = pygame.transform.scale(img , (int(img.get_width() * scale),int ( img.get_height()* scale)))
           # حفظ الصورة في مستطيل
           self.rect= self.image.get_rect()
           # المستطيل يتم حفظ موقعه في اكس  و واي
           self.rect.center = (x,y)


       def draw (self):
           screen.blit(self.image , self.rect)

           
player = Soldier(200, 200 ,3) 




###################### GAME LOOP ################################
run = True 

while run :


       player.draw()
      ###########  DRAWING  ###################
       for event in pygame.event.get():
           if event.type == pygame.QUIT :
                 run = False
       pygame.display.update()

       
pygame.quit()                 

import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = int(SCREEN_WIDTH) * 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Creating game window
pygame.display.set_caption("Dinnerdash")
#Giving a window title

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite. __init__(self)
        img = pygame.image.load(r'image\cook.png')
        self.image = pygame.transform.scale(img, (int(img.get_width()* scale), int(img.get_height()* scale)))
        self.rect = self.image.get_rect()
        #Takes the siwe of the image and creates a boundary box around it, to control position and collision
        self.rect.center= (x,y)

    def draw(self):
          screen.blit(self.image, self.rect)
#To keep the code running, we have to  use a while loop

cook = Player(200, 300, 0.03)
#Coordinates where I want to draw the player


run = True
#As long as this variable remains in the true condition, the while loop will be executed
while run:

    cook.draw()
 
    for event in pygame.event.get():
    #Creating an interaction to quit the game
         if event.type == pygame.QUIT:
            run =  False

    pygame.display.update()

pygame.quit()

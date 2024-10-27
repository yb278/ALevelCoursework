import pygame, sys 
from pygame import mixer
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.mixer.init()

#sets the caption title and image
pygame.display.set_caption('Arcade shooter')
pygame_icon = pygame.image.load('icon.png')
pygame.display.set_icon(pygame_icon)

screen_width = 1200
screen_height = 1000

global screen
screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE|SCALED)

#loading of background image
bg_img = pygame.image.load('background1.jpg')
background_update = pygame.transform.scale(bg_img,(screen_width,screen_height))

#setting font settings
font = pygame.font.Font('font.ttf', 30)

# color encoding
white = (255,255,255)
black = (0,0,0)

#function that draws text in a colored font on the screen at any coordinate
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

f = open("score.txt", "r")
final_score = f.read()

def main():
    while True:
        screen.blit(background_update,(0,0))
        #Draw backdrops for text
        f_box = pygame.Rect((screen_width/2) -200, (screen_height/3.3) + 100, 350, 40)
        pygame.draw.rect(screen, black, f_box)
        
        t_box = pygame.Rect((screen_width/2) -200, (screen_height/3.3) + 200, 280, 40)
        pygame.draw.rect(screen, black, t_box)

        draw_text('Final score:'+str(final_score), font, white, screen, (screen_width/2) -200, (screen_height/3.3) + 100)
        draw_text('Thanks for playing', font, white, screen,(screen_width/2) -200, (screen_height/3.3) + 200)
        
        #Event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.update()
        mainClock.tick(60)
        pygame.time.wait(5000)
        import menu
    
main()

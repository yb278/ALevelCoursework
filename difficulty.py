import pygame, sys 
from pygame import mixer
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.mixer.init()

#loads audio files for game and interactions
click_sound = pygame.mixer.Sound('button_press.wav')
mixer.music.load('menu_music.mp3')
mixer.music.play()

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
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


#function that draws text in a colored font on the screen at any coordinate
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#Used in validation of when a button is pressed
global click
click = False



def main_menu():
    click = False
    while True:
        screen.blit(background_update,(0,0))

        draw_text('Please Select a Difficulty', font, white, screen, (screen_width/2) -200, 80)
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect((screen_width/2) -200, (screen_height/10) + 100, 120, 40)
        button_2 = pygame.Rect((screen_width/2) -200, (screen_height/5) + 100, 120, 40)
        button_3 = pygame.Rect((screen_width/2) -200, (screen_height/3.3) + 100, 130, 40)
        
        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                click_sound.play()
                easy()
        if button_2.collidepoint((mx, my)):
            if click:
                click_sound.play()
                medium()
        if button_3.collidepoint((mx, my)):
            if click:
                click_sound.play()
                hard()
    
        #Draws a black box for the button
        pygame.draw.rect(screen, black, button_1)
        pygame.draw.rect(screen, black, button_2)
        pygame.draw.rect(screen, black, button_3)
        
        #writing text on top of button
        draw_text('Easy', font, white, screen, (screen_width/2) -200, (screen_height/10) + 100)
        draw_text('Medium', font, white, screen, (screen_width/2) -200, (screen_height/5) + 100)
        draw_text('Hard', font, white, screen, (screen_width/2) -200, (screen_height/3.3) + 100)
        click = False
        
        #Event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 

def easy():
    f = open("settings.txt", "w")
    f.write("Easy")
    f.close()
    pygame.time.wait(1000)
    import game

def medium():
    f = open("settings.txt", "w")
    f.write("Medium")
    f.close()
    pygame.time.wait(1000)
    import game
    
def hard():
    f = open("settings.txt", "w")
    f.write("Hard")
    f.close()
    pygame.time.wait(1000)
    import game


def quit():
    pygame.quit()
    sys.exit()
main_menu()

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

        draw_text('Welcome player', font, white, screen, (screen_width/6), 40)
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect((screen_width/6), (screen_height/10), 120, 40)
        button_2 = pygame.Rect((screen_width/6), (screen_height/5), 120, 40)
        button_3 = pygame.Rect((screen_width/6), (screen_height/3.3), 130, 40)
        button_4 = pygame.Rect((screen_width/6), (screen_height/2.5), 120, 40)
        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                click_sound.play()
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                click_sound.play()
                instructions()
        if button_3.collidepoint((mx, my)):
            if click:
                click_sound.play()
                options()
        if button_4.collidepoint((mx, my)):
            if click:
                click_sound.play()
                quit()
        
        #Draws a black box for the button
        pygame.draw.rect(screen, black, button_1)
        pygame.draw.rect(screen, black, button_2)
        pygame.draw.rect(screen, black, button_3)
        pygame.draw.rect(screen, black,button_4)
        
        #writing text on top of button
        draw_text('PLAY', font, white, screen, (screen_width/6), (screen_height/10))
        draw_text('INFO', font, white, screen, (screen_width/6), (screen_height/5))
        draw_text('OPTIONS', font, white, screen, (screen_width/6), (screen_height/3.3))
        draw_text('QUIT', font, white, screen, (screen_width/6), (screen_height/2.5))
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
 

def game():
    pygame.time.wait(1000)
    import difficulty
    

def options():
    running = True
    click = False
    while running:
        screen.blit(background_update,(0,0))
        mx, my = pygame.mouse.get_pos()
        button_s = pygame.Rect(screen_width/2.4, screen_height/10, 230, 40)
        
        if button_s.collidepoint((mx, my)):
            if click:
                click_sound.play()
                sound_settings()
        
        pygame.draw.rect(screen, black, button_s)
        
        draw_text('Sound Settings', font, white, screen, screen_width/2.4, screen_height/10)
        click = False
        
        draw_text('OPTIONS SCREEN', font, white, screen,screen_width/60, screen_height/50)
        draw_text('Press ESC to go back', font, white, screen,screen_width/60, screen_height/1.7)
        
        #event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
 
def instructions():
    running = True
    while running:
        screen.blit(background_update,(0,0))
        
        draw_text('INFO', font, white, screen, screen_width/60, screen_height/50)
        draw_text('Game Objective', font, white,screen, screen_width/60, screen_height/10)
        draw_text('The objective of the game is to take down enemies and avoid attacks for as', font, white, screen, screen_width/60, screen_height/7.7)
        draw_text('long as possible.', font, white, screen,screen_width/60, screen_height/6.5)
        draw_text('Game controls', font, white, screen,screen_width/60, screen_height/5)
        draw_text('Use the arrow keys or WASD keys to move your ship around the screen.', font, white, screen,screen_width/60, screen_height/4.3)
        draw_text('Use SPACE to fire a bullet, and use SHIFT to slow down.', font, white, screen,screen_width/60, screen_height/3.9)
        draw_text('Upgrades', font, white, screen,20,300)
        draw_text("As you reach a score an upgrade will appear", font, white, screen,screen_width/60, screen_height/3)
        draw_text("Use these power-ups to upgrade your ship's weapon.", font, white, screen,screen_width/60, screen_height/2.8)
        draw_text('Scoring', font, white, screen,screen_width/60, screen_height/2.5)
        draw_text('You will earn points for each enemy you destroy.', font, white, screen,screen_width/60, screen_height/2.3)
        draw_text('Your score can increase at a quicker rate depending on the enemy difficulty', font, white, screen,screen_width/60, screen_height/2.19)
        draw_text('Press ESC to go back', font, white, screen,screen_width/60, screen_height/1.7)
        
        #event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

def sound_settings():
    running = True
    click = False
    volume = 5

    while running:
        screen.blit(background_update,(0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text('Sound settings', font, white, screen,screen_width/60, screen_height/50)
        draw_text('Press ESC to go back', font, white, screen,screen_width/60, screen_height/1.7)

        increase_vol = pygame.Rect(screen_width/2, screen_height/10, 50, 40)
        decrease_vol = pygame.Rect(screen_width/6, screen_height/10, 50, 40) 

        if increase_vol.collidepoint((mx, my)):
            if click:
                click_sound.play()
                if volume < 10:
                    volume += 1
                    mixer.music.set_volume(volume/10)

        if decrease_vol.collidepoint((mx, my)):
            if click:
                click_sound.play()
                if volume >0:
                    volume -=1 
                    mixer.music.set_volume(volume/10)

        click = False
        pygame.draw.rect(screen, green, increase_vol)
        pygame.draw.rect(screen, red, decrease_vol)

        draw_text(str(volume)+"0%" , font, white, screen, screen_width/3, screen_height/10)
        draw_text('+', font, black, screen,screen_width/1.95, screen_height/10)
        draw_text('-', font, black, screen, screen_width/5.6, screen_height/10)

        #event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()     
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False  
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)


def quit():
    pygame.quit()
    sys.exit()
main_menu()
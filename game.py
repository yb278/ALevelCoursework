import pygame, sys, random
from pygame import mixer
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.mixer.init()
import math
import time



#Display setup
screen_size = [1500,1000]
screen = pygame.display.set_mode((screen_size), RESIZABLE|SCALED)

#Shows title and the icon 
pygame.display.set_caption("Game")
pygame_icon = pygame.image.load('icon.png')
pygame.display.set_icon(pygame_icon)

#Playes the music for the game
mixer.music.load('game_music.mp3')
mixer.music.play()

#Loads sound effects
player_fire =pygame.mixer.Sound('laser.mp3')#Player fire laser
bonus = pygame.mixer.Sound('bonus.wav')#Kill count eached
ship_destroy = pygame.mixer.Sound('ship_destroy.wav')#Enemy ship destroyed 1
ship_destroy2 = pygame.mixer.Sound('ship_destroy2.wav')#Enemy ship destroyed 2
player_damage = pygame.mixer.Sound('player_hit.wav')#Player damage taken
pause = pygame.mixer.Sound('pause.wav')#Pause game
player_defeat = pygame.mixer.Sound('player_defeat.wav')#Played on loss 
upgrade_sound = pygame.mixer.Sound('upgrade.wav')#Upgrade sound
click_sound = pygame.mixer.Sound('button_press.wav')#Brought back click sound for menu

#Pause menu images
p_img = pygame.image.load('background1.jpg')
pause_menu = pygame.transform.scale(p_img,(screen_size[0],screen_size[1]))


#Reading the text file to see the difficulty
f = open("settings.txt", "r")
Difficulty = f.read()

#Loads ship image and scales it down
ship_image = pygame.image.load('ship.png')
ship_image = pygame.transform.scale(ship_image, (100, 100))

#Loading of 'booster' flame image and scaling it down
flame_image = pygame.image.load('flame.png')
flame_image = pygame.transform.scale(flame_image, (20,40))

#Loading and scaling of enemy ship
enemy1_image = pygame.image.load('enemy1.png')
enemy1_image = pygame.transform.scale(enemy1_image, (70,70))

#Enemy 2 image
enemy2_image = pygame.image.load('enemy2.png')
enemy2_image = pygame.transform.scale(enemy2_image, (70,70))

#Enemy 3 image 
enemy3_image = pygame.image.load('enemy3.png')
enemy3_image = pygame.transform.scale(enemy3_image, (70,70))

#Load image and scale it down
laser_image = pygame.image.load('laser.png')
laser_image = pygame.transform.scale(laser_image,(20,60))


#Variables to manage waves 
current_wave = 1
score_needed =5000

# color encoding
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (128, 128, 128)
yellow =(234, 221, 202)

#Validation of where the player is moving
is_moving_up = False
is_moving_left = False
is_moving_down = False
is_moving_right = False
shift_down = False

#setting font settings
font = pygame.font.Font('font.ttf', 22)

#Used to check if upgrade occurs
upgrade_yn = False


#function that draws text in a colored font on the screen at any coordinate
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#Function for pausing the game
def paused():
    #Necessary values
    running = True
    click = False
    pause.play()
    while running:
        #What the menu looks like
        screen.blit(pause_menu,(0,0))
        mx, my = pygame.mouse.get_pos()
        button_s = pygame.Rect(screen_size[0]/2.4, screen_size[1]/10, 170, 40)
        button_q = pygame.Rect((screen_size[0]/2.4), (screen_size[1]/5), 120, 40)
        
        #Sound settings 
        if button_s.collidepoint((mx, my)):
            if click:
                click_sound.play()
                sound_settings()
        if button_q.collidepoint((mx, my)):
            if click:
                click_sound.play()
                game_end()


        pygame.draw.rect(screen, black, button_s)
        draw_text('Sound Settings', font, white, screen, screen_size[0]/2.4, screen_size[1]/10)
        pygame.draw.rect(screen, black, button_q)
        draw_text('End Game', font, white, screen, screen_size[0]/2.4, screen_size[1]/5)
        
        click = False
        
        #Basic instructions 
        draw_text('OPTIONS SCREEN', font, white, screen,screen_size[0]/60, screen_size[1]/50)
        draw_text('Press P to resume', font, white, screen,screen_size[0]/60, screen_size[1]/1.7)
        
        #event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    pause.play()
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)

#Sound settings from the menu page
def sound_settings():
    running = True
    click = False
    volume = 5

    while running:
        screen.blit(pause_menu,(0,0))
        mx, my = pygame.mouse.get_pos()
        
        draw_text('Sound settings', font, white, screen,screen_size[0]/60, screen_size[1]/50)
        draw_text('Press ESC to go back', font, white, screen,screen_size[0]/60, screen_size[1]/1.7)

        increase_vol = pygame.Rect(screen_size[0]/2, screen_size[1]/10, 50, 40)
        decrease_vol = pygame.Rect(screen_size[0]/6, screen_size[1]/10, 50, 40) 

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

        draw_text(str(volume)+"0%" , font, white, screen, screen_size[0]/3, screen_size[1]/10)
        draw_text('+', font, black, screen,screen_size[0]/1.95, screen_size[1]/10)
        draw_text('-', font, black, screen, screen_size[0]/5.6, screen_size[1]/10)

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


class ship(object):
    def __init__(self, x, y, ship_image, flame_image):
        self.x = 500
        self.y = 800
        self.health = 0
        self.damage = 0 
        self.speed = 10
        self.image = ship_image
        self.flame = flame_image
        self.hitbox = (self.x, self.y, 100, 100)
        self.score = 0
        self.kill_count = 0
        self.max_health = 0

        #Sets player stats
        if Difficulty == "Easy":
            self.health = 200
            self.max_health = 200
            self.damage = 50
        if Difficulty == "Medium":
            self.health = 100
            self.max_health = 100
            self.damage = 25
        if Difficulty == "Hard":
            self.health = 50
            self.max_health = 50
            self.damage = 25

    def move(self, direction):
        #If moving the coordinates will update
        if direction == "up":
            self.y -= self.speed
        if direction == "left":
            self.x -= self.speed
        if direction == "down":
            self.y += self.speed
        if direction == "right":
            self.x += self.speed
         
        #makes sure that the player does not go into the boundaries 
        if self.y < 0:
            self.y = 0
        elif self.y > screen_size[1] - 100:
           self.y = screen_size[1] - 100

        if self.x < 300:
            self.x = 300
        elif self.x > screen_size[0] - 100:
            self.x = screen_size[0] - 100

    def update(self):
        screen.blit(self.image, (self.x,self.y))
        playerrect.center = (player.get_posx()+50, player.get_posy()+75)
        if is_moving_up == True:
            screen.blit(self.flame, (self.x +22, self.y + 80))
            screen.blit(self.flame, (self.x +59, self.y + 80 ))
        #Makes sure hitbox follows the player
        self.hitbox = (self.x, self.y, 100, 100)
        #pygame.draw.rect(screen,(0,255,0), self.hitbox, 2)
        
    def enemy_killed(self, type):
        if type == 1: #Laser with enemy
            self.score += 300
            self.kill_count +=1

        if type == 2: #Player with enemy 
            self.score -= 50
            self.kill_count += 1

    def slow_down(self):
        self.speed = 5
    
    def normal_speed(self):
        self.speed = 10 
        
    def get_posx(self):
        return self.x
    def get_posy(self):
        return self.y

player = ship(500, 500, ship_image, flame_image)
#Create a rectangle around the ship image for collisions
playerrect = ship_image.get_rect()


def game_end():
    f = open("score.txt", "w")
    f.write(str(player.score))
    f.close()
    pygame.time.wait(1000)
    pygame.mixer.music.pause()
    player_defeat.play()
    #Then give a screen showing score and after 5 seconds take back to main menu
    import game_end

def upgrade(score):
    global upgrade_yn 
    
    if upgrade_yn ==  False:
        upgrade_sound.play()

        #Necessary values
        running = True
        click = False
        while running:
            #What the menu looks like
            screen.blit(pause_menu,(0,0))
            mx, my = pygame.mouse.get_pos()
            button_1 = pygame.Rect(screen_size[0]/2.4, screen_size[1]/10, 150, 40)
            button_2 = pygame.Rect((screen_size[0]/2.4), (screen_size[1]/5), 150, 40)
            
            #Sound settings 
            if button_1.collidepoint((mx, my)):
                if click:
                    click_sound.play()
                    player.health += 50
                    running = False
                    upgrade_yn = True
            if button_2.collidepoint((mx, my)):
                if click:
                    click_sound.play()
                    player.damage += 25
                    running = False
                    upgrade_yn = True

            pygame.draw.rect(screen, black, button_1)
            draw_text('+50 health', font, white, screen, screen_size[0]/2.4, screen_size[1]/10)
            pygame.draw.rect(screen, black, button_2)
            draw_text('+25 Damage', font, white, screen, screen_size[0]/2.4, screen_size[1]/5)
            
            click = False
            #Basic instructions 
            draw_text('UPGRADE !!!', font, white, screen,screen_size[0]/60, screen_size[1]/50)
            draw_text('Press P to resume', font, white, screen,screen_size[0]/60, screen_size[1]/1.7)
            
            #event handler
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        pause.play()
                        running = False
                        upgrade_yn = True#Stop it from looping
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()
            mainClock.tick(60)
    else:
        running = False
    


class enemy_ship(ship):
    def __init__(self, x, y, ship_image):
        super().__init__(x, y,ship_image, flame_image)
        self.x = x
        self.y = y
        self.health = 0
        self.damage = 0
        self.speed = 0
        self.image = ship_image
        self.hitbox = (self.x, self.y, 70, 70)
        self.enemy_type = 0 
        self.shoot_timer = 0
        self.max_health = 0

        self.enemyrect = ship_image.get_rect()
        self.enemyrect.center = (self.x+35, self.y+35)

        if Difficulty == "Easy":
            self.health = 50
            self.max_health = 50
            self.damage = 10
        if Difficulty == "Medium":
            self.health = 100
            self.max_health = 100
            self.damage = 15
        if Difficulty == "Hard":
            self.health = 150
            self.max_health = 150
            self.damage = 50

        if current_wave == 2:
            self.damage += 20
            self.health += 20
            self.max_health +=20
        elif current_wave ==3:
            self.damage += 30
            self.health += 100
            self.max_health += 100

    def draw(self):
        screen.blit(self.image, (self.x,self.y))
        self.hitbox = (self.x , self.y, 70, 70)

    def fire(self):
        shoot_enemy_projectiles(self, 2)
    
    
class projectile(object):
    def __init__(self,x,y,laser_image, angle , speed ):
        self.x = x
        self.y = y
        self.image = laser_image
        self.vel = 10 
        self.angle = angle
        self.speed = speed
        
        self.laserrect = laser_image.get_rect()
        
    #Draw the image at the player coordinates
    def player_draw(self):
        screen.blit(self.image, (self.x -10 , self.y - 40))
        
enemy_lasers = []

class enemy_laser():
    # A projectile that can be shot from an enemy.
    def __init__(self, x, y, angle, speed):
        # Initializes the projectile.
        self.x = x +35
        self.y = y+ 70
        self.angle = angle
        self.speed = speed
        self.color = red

        
        if current_wave == 2:
            self.color = blue
        elif current_wave == 3:
           self.color = yellow
        

    def update(self):
        # Updates the position of the projectile.
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

        # Check if the projectile is off screen.
        if self.x < 0 or self.x > screen_size[0] or self.y < 0 or self.y > screen_size[1]:
            # Delete the projectile.
            enemy_lasers.remove(self)

    def draw(self):
        # Draws the projectile.
        pygame.draw.circle(screen, self.color,(self.x,self.y) , 3)
        
    def give_hitbox_pos(self):
        hitbox = pygame.Rect(self.x,self.y,6,6)
        return(hitbox)

def shoot_enemy_projectiles(enemy, number_of_proj):
    # Shoots a number of projectiles in a circular pattern from the enemy.
    
    for i in range(number_of_proj):
        chance = random.randint(1, 100)
        if chance > 98:
            angle = random.uniform(0, 3)
            speed = random.uniform(1, 2)
            new_proj = enemy_laser(enemy.get_posx(), enemy.get_posy(), angle, speed)
            enemy_lasers.append(new_proj)

        # Add a gap between each bullet.
        if i < number_of_proj - 1:
            time.sleep(0.00000000000000005)#Has to be large as it slows the game down really vastly 

    for laser in enemy_lasers:
        laser.draw()
        laser.update()


#Event handler function 
def event_handler(event):
    global ship, is_moving_up, is_moving_left, is_moving_down, is_moving_right, is_shooting, shift_down
    # Check for keyboard events
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            is_moving_up = True
        elif event.key == pygame.K_a:
            is_moving_left = True
        elif event.key == pygame.K_s:
            is_moving_down = True
        elif event.key == pygame.K_d:
            is_moving_right = True
        elif event.key == pygame.K_SPACE:
            #Max of 10 bullets on screen
            if len(bullets) < 10:
                bullet = projectile(player.get_posx() + 50,player.get_posy(), laser_image, 0 ,0)
                bullets.append(bullet)
                player_fire.play()
        #Shift slows the charcter down for more precise movements
        elif event.key == pygame.K_LSHIFT:
            shift_down = True
        elif event.key == pygame.K_p:
            paused()
            
    #When key lifted player no longer moving
    elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                is_moving_up = False
            elif event.key == pygame.K_a:
                is_moving_left = False
            elif event.key == pygame.K_s:
                is_moving_down = False
            elif event.key == pygame.K_d:
                is_moving_right = False
            elif event.key == pygame.K_LSHIFT:
                shift_down = False
                
#Menu updating system
def UI():
    #Main outline
    menu = pygame.Rect(0, 0, 300, 1000)
    pygame.draw.rect(screen, grey, menu )
    #Border
    border =pygame.Rect(0,0,300, 1000)
    pygame.draw.rect(screen, green, border, 1)
    #Score text
    draw_text('Score: ' + str(player.score), font, black, screen, 5 ,50)
    #Wave num
    draw_text('Wave:' + str(current_wave), font, black, screen, 5, 150 )
    #Enemy kill count
    draw_text('Enemies Destroyed:'+ str(player.kill_count), font, black, screen, 5, 250)
    
    #Points till next wave
    if player.score > 15000:
        draw_text('Last wave', font, black, screen, 5, 350)
    else:
        draw_text('Next wave in:'+ str(score_needed- player.score), font, black, screen, 5, 350)
    
    #Shows how much damage and the speed the player has 
    draw_text('Speed:' + str(player.speed), font, black, screen, 5, 450)
    draw_text('Damage:'+ str(player.damage), font, black, screen, 5, 550)
    #Current enemy health
    draw_text('Enemy Health:'+ str(enemy.max_health), font, black, screen, 5, 650)
    #Difficulty
    draw_text('Difficulty:' +str(Difficulty), font, black, screen, 5, 750)

    #Healthbar code
    health_bar_width = 290 #Default width
    health_bar_width_decrease = (1 - player.health / player.max_health) * health_bar_width #Formula
    health_bar_width -= health_bar_width_decrease #Decreases it uniformly

    #Draws in both bars
    pygame.draw.rect(screen, red, (5,900,290,40), 0, 10)
    pygame.draw.rect(screen, green, (5,900,(health_bar_width),40), 0, 10)

#All update functions occur here
def update_window():
    #Fills the background 
    screen.fill(black)
    #Update player position
    player.update()
    #Draw all enemies on screen
    for enemy in enemies:
        enemy.draw()
        enemy.fire()
        
    #Draw all bullets 
    for bullet in bullets:
        bullet.player_draw()
    #Draw the UI and update it 
    UI()

    #For each laser check for collision
    for enemy_laser in enemy_lasers:
        if playerrect.colliderect(enemy_laser.give_hitbox_pos()):
                player.health -= enemy.damage
                player_damage.play()
                enemy_lasers.pop(enemy_lasers.index(enemy_laser))


    pygame.display.update()
    
#Lists for bullets 
bullets = []
enemies =[]


#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        event_handler(event)

    if shift_down:
        player.slow_down()
    else:
        player.normal_speed()
    if is_moving_up:
        player.move("up")
    if is_moving_right:
        player.move("right")
    if is_moving_down:
        player.move("down")
    if is_moving_left:
        player.move("left")
    
    
    #Depending on the wave, the image and difficulty of the enemy will change 
    if current_wave == 1:
        if len(enemies) == 0:
            for i in range(0,5):
                x = random.randint(300,1400)
                y = random.randint(0,400)
                enemies.append(enemy_ship(x,y, enemy1_image))
    
    elif current_wave == 2:
        if len(enemies) == 0:
            for i in range(0,5):
                x = random.randint(300,1400)
                y = random.randint(0,400)
                enemies.append(enemy_ship(x,y, enemy2_image))
    else:
        if len(enemies) == 0:
            for i in range(0,5):
                x = random.randint(300,1400)
                y = random.randint(0,400)
                enemies.append(enemy_ship(x,y, enemy3_image))
            
    for enemy in enemies:
        #Check bounds of the enemy 
        if enemy.y < screen_size[0] and enemy.y > 0:
            pass
        else:
            enemies.pop(enemies.index(enemy))
        #Pop enemy when health is 0
        if enemy.health <= 0:
            enemies.pop(enemies.index(enemy))
            
            #Random destroy sound
            ran_num = random.randint(0,1)
            if ran_num == 0:
                ship_destroy.play()
            else:
                ship_destroy2.play()

            player.enemy_killed(1)
        
        for bullet in bullets:
            if bullet.laserrect.colliderect(enemy.enemyrect):
                enemy.health -= player.damage
                bullet.y = -10
        
        #Player collision
        if playerrect.colliderect(enemy.enemyrect):
            player.health -= 10
            player_damage.play()
            enemies.pop(enemies.index(enemy))
            
            #Random destroy sound
            ran_num = random.randint(0,1)
            if ran_num == 0:
                ship_destroy.play()
            else:
                ship_destroy2.play()

            player.enemy_killed(2)

    #for each bullet update hit box and check if on screen 
    for bullet in bullets:
        bullet.laserrect.center = (bullet.x+10, bullet.y+30)
        if bullet.y < screen_size[0] and bullet.y >0:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
        


    #Death of player
    if player.health <= 0:
        game_end()
   
    #Wave 2
    if player.score >= 5000:
        current_wave = 2
        score_needed = 15000
        
    #Wave 3 
    if player.score >= 15000:
        current_wave = 3
    
    #Bonus points 
    if player.kill_count == 50:
        player.score += 500
        bonus.play()
    if player.kill_count == 100:
        player.score += 1000
        bonus.play()

    
    if player.score >= 8000:
        upgrade(player.score)
       
    if player.score >=16000:
        upgrade(player.score)
       

    update_window()
    pygame.time.Clock().tick(120)
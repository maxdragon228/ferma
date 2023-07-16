from pygame import *
import sys
from random import randint

init()

font.init()

text1 = font.SysFont ("Arial",40)

text2 = font.SysFont ("Timesnewroman",90)

text3 = font.SysFont ("Timesnewroman",90)

text4 = font.SysFont ("Timesnewroman",30)

text5 = font.SysFont("Arial",60)

shop_exit_img = image.load("shop_exit.png")

invertar = image.load("inventar.png")

play_img = image.load("play.png")

plant_1_img = image.load("plant_1_img.png")

plant_2_img = image.load("plant_2_img.png")

plant_3_img = image.load("plant_3_img.png")

plant_4_img = image.load("plant_4_img.png")

plant_5_img = image.load("plant_5_img.png")

plant_6_img = image.load("plant_6_img.png")

plant_7_img = image.load("plant_7_img.png")

plant_8_img = image.load("plant_8_img.png")

plant_9_img = image.load("plant_9_img.png")

plant_10_img = image.load("plant_10_img.png")

plant_11_img = image.load("plant_11_img.png")

plant_12_img = image.load("plant_12_img.png")

pick_img = image.load("pick.png")

settings_img = image.load("settings.png")

exit_img = image.load("exit.png")

ogorod_image = image.load("ogorod.png")

volume1_image = image.load("VOL_1.png")

volume2_image = image.load("VOL_2.png")

volume3_image = image.load("VOL_3.png")

volume4_image = image.load("VOL_4.png")

back_img = image.load("back.png")

tomato_img = image.load("tomato.png")

carrot_img = image.load("carrot.png")

potato_button_png = image.load("potato_png.png")

tomato_button_png = image.load("tomato_png.png")

carrot_seed_img = image.load("carrot_seed_img.png")

potato_seed_img = image.load("potato_seed_img.png")

tomato_seed_img = image.load("tomato_seed_img.png")

shop_menu_img = image.load("shop_menu_img.png")

carrot_button_png = image.load("carrot_png.png")

potato_img = image.load("potato.png")

money_img = image.load("money.png")

clock= time.Clock()

font = font.SysFont(None, 20)

mixer.init()

press = mixer.Sound("music/press.ogg")

mixer.music.load("music/fon_music.ogg")

mixer.music.play()

class GameSprite(sprite.Sprite):
    
    def __init__(self, s_image, player_x, player_y,size_x,size_y ,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(s_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    
    def update(self):
        keys = key.get_pressed()

        if (keys[K_a] ^ keys[K_LEFT]) and self.rect.x > 0:
            self.rect.x -= self.speed

        if (keys[K_d] ^ keys[K_RIGHT]) and self.rect.x < 1180:
            self.rect.x += self.speed

        if (keys[K_w] ^ keys[K_UP]) and self.rect.y > 0:
            self.rect.y -= self.speed

        if (keys[K_s] ^ keys[K_DOWN]) and self.rect.y < 620:
            self.rect.y += self.speed

        if (keys[K_LEFT] ^ keys[K_a]) and self.rect.x > 0:
            self.rect.x -= self.speed

        if (keys[K_RIGHT] ^ keys[K_d]) and self.rect.x < 1180:
            self.rect.x += self.speed

        if (keys[K_UP] ^ keys[K_w]) and self.rect.y > 0:
            self.rect.y -= self.speed

        if (keys[K_DOWN] ^ keys[K_s]) and self.rect.y < 620:
            self.rect.y += self.speed

class Button():
    
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = transform.scale(image,(int(width * scale),int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = x,y
        self.clicked = False

    def draw(self,mw):
        action = False
        pos = mouse.get_pos()

        if self.rect.collidepoint(pos):
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                mixer.Sound.play(press)
                self.clicked = True
                action = True

        if mouse.get_pressed()[0] == 0:
            self.clicked = False
        mw.blit(self.image, (self.rect.x,self.rect.y))
        return action

class Ogorod(sprite.Sprite):
    
    def __init__(self, plant_image, plant_x, plant_y,size_x,size_y):
        self.image = transform.scale(image.load("ogorod.png"), (size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = plant_x
        self.rect.y = plant_y
        self.planted = False

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
        
        
play_button = Button(450,300,play_img,1)

ogorod_button_buy = Button(580, 400, ogorod_image,1)

settings_button = Button(550,300,settings_img,1)

exit_button = Button(650,300,exit_img,1)

shop_plant_tomato = Button(200,170,tomato_seed_img,1)

shop_plant_potato = Button(580,170,potato_seed_img,1)

shop_plant_carrot = Button(970,170,carrot_seed_img,1)

shop_exit = Button(470,20,shop_exit_img,1)

plant_tomato = Button(450,300,tomato_button_png,1)

plant_carrot = Button(700,300,carrot_button_png,1)

plant_potato = Button(575,300,potato_button_png,1)

back_button = Button(725,300,back_img,1)

back_button_plant = Button(575,400,back_img,1)

volume_button = Button(425,300,volume3_image,1)

volume1_button = Button(575,175,volume1_image,1)

volume2_button = Button(575,275,volume2_image,1)

volume3_button = Button(575,375,volume3_image,1)

volume4_button = Button(575,475,volume4_image,1)

text_col = (255,255,255)

menu_state = "main"

money = 0

now_time = 10

game_paused = True

dis_x = 1280

dis_y = 720

FPS = 100

speed = 1

finish = False

manual = True

game = True

plant_seed_1 = False

plant_seed_2 = False

plant_seed_3 = False

plant_seed_4 = False

plant_seed_5 = False

plant_seed_6 = False

plant_seed_7 = False

plant_seed_8 = False

plant_seed_9 = False

plant_seed_10 = False

plant_seed_11 = False

plant_seed_12 = False

map = transform.scale(image.load("map.png"),(1280,720))

mw = display.set_mode((dis_x,dis_y))

shop = GameSprite("shop.png",50,150,307,293,0)

player = Player("player.png",300,500,100,100,5)

pick_button = Button(player.rect.x,player.rect.y - 150,pick_img,1)

ogorod_1 = Ogorod('ogorod.png', 1160, 20, 100, 100) 

ogorod_2 = Ogorod('ogorod.png', 1050, 20, 100, 100) 

ogorod_3 = Ogorod('ogorod.png', 1050, 130, 100, 100) 

ogorod_4 = Ogorod('ogorod.png', 1160, 130, 100, 100) 

ogorod_5 = Ogorod('ogorod.png', 1050, 240, 100, 100) 

ogorod_6 = Ogorod('ogorod.png', 1160, 240, 100, 100) 

ogorod_7 = Ogorod('ogorod.png', 1050, 350, 100, 100) 

ogorod_8 = Ogorod('ogorod.png', 1160, 350, 100, 100) 

ogorod_9 = Ogorod('ogorod.png', 1050, 460, 100, 100) 

ogorod_10 = Ogorod('ogorod.png', 1160, 460, 100, 100) 

ogorod_11 = Ogorod('ogorod.png', 1050, 570, 100, 100) 

ogorod_12 = Ogorod('ogorod.png', 1160, 570, 100, 100) 

coin_1 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coin_2 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coin_3 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coin_4 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coin_5 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coin_6 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coin_7 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coin_8 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coin_9 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coin_10 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coin_11 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coin_12 = GameSprite('coin.png', 200, 200, 100, 100, 1)

coins = sprite.Group()

plants = sprite.Group()

state_coin_1 = 0

state_coin_2 = 0

state_coin_3 = 0

state_coin_4 = 0

state_coin_5 = 0

state_coin_6 = 0

state_coin_7 = 0

state_coin_8 = 0

state_coin_9 = 0

state_coin_10 = 0

state_coin_11 = 0

state_coin_12 = 0

tomato_seed = 5

carrot_seed = 0

potato_seed = 0

game = True

state_ogorod_1 = False

state_ogorod_2 = False

state_ogorod_3 = False

state_ogorod_4 = False

state_ogorod_5 = False

state_ogorod_6 = False

state_ogorod_7 = False

state_ogorod_8 = False

state_ogorod_9 = False

state_ogorod_10 = False

state_ogorod_11 = False

state_ogorod_12 = False

now_time_1 = 10

now_time_2 = 10

now_time_3 = 10

now_time_4 = 10

now_time_5 = 10

now_time_6 = 10

now_time_7 = 10

now_time_8 = 10

now_time_9 = 10

now_time_10 = 10

now_time_11 = 10

now_time_12 = 10

state_plant_1 = 0

state_plant_2 = 0

state_plant_3 = 0

state_plant_4 = 0

state_plant_5 = 0

state_plant_6 = 0

state_plant_7 = 0

state_plant_8 = 0

state_plant_9 = 0

state_plant_10 = 0

state_plant_11 = 0

state_plant_12 = 0

shop_menu_state = True

plant_menu_state = True

state_menu = True

tomato_1 = GameSprite("plant_seed.png", ogorod_1.rect.x, ogorod_1.rect.y, 70, 100 , 0) 

tomato_2 = GameSprite("plant_seed.png", ogorod_2.rect.x, ogorod_2.rect.y, 70, 100 , 0) 

tomato_3 = GameSprite("plant_seed.png", ogorod_3.rect.x, ogorod_3.rect.y, 70, 100 , 0) 

tomato_4 = GameSprite("plant_seed.png", ogorod_4.rect.x, ogorod_4.rect.y, 70, 100 , 0) 

tomato_5 = GameSprite("plant_seed.png", ogorod_5.rect.x, ogorod_5.rect.y, 70, 100 , 0) 

tomato_6 = GameSprite("plant_seed.png", ogorod_6.rect.x, ogorod_6.rect.y, 70, 100 , 0) 

tomato_7 = GameSprite("plant_seed.png", ogorod_7.rect.x, ogorod_7.rect.y, 70, 100 , 0) 

tomato_8 = GameSprite("plant_seed.png", ogorod_8.rect.x, ogorod_8.rect.y, 70, 100 , 0) 

tomato_9 = GameSprite("plant_seed.png", ogorod_9.rect.x, ogorod_9.rect.y, 70, 100 , 0) 

tomato_11 = GameSprite("plant_seed.png", ogorod_10.rect.x, ogorod_10.rect.y, 70, 100 , 0) 

tomato_10 = GameSprite("plant_seed.png", ogorod_11.rect.x, ogorod_11.rect.y, 70, 100 , 0) 

tomato_12 = GameSprite("plant_seed.png", ogorod_12.rect.x, ogorod_12.rect.y, 70, 100 , 0) 

carrot_1 = GameSprite("plant_seed.png", ogorod_1.rect.x, ogorod_1.rect.y, 70, 100, 0) 

carrot_2 = GameSprite("plant_seed.png", ogorod_2.rect.x, ogorod_2.rect.y, 70, 100, 0) 

carrot_3 = GameSprite("plant_seed.png", ogorod_3.rect.x, ogorod_3.rect.y, 70, 100, 0) 

carrot_4 = GameSprite("plant_seed.png", ogorod_4.rect.x, ogorod_4.rect.y, 70, 100, 0) 

carrot_5 = GameSprite("plant_seed.png", ogorod_5.rect.x, ogorod_5.rect.y, 70, 100, 0)

carrot_6 = GameSprite("plant_seed.png", ogorod_6.rect.x, ogorod_6.rect.y, 70, 100, 0) 

carrot_7 = GameSprite("plant_seed.png", ogorod_7.rect.x, ogorod_7.rect.y, 70, 100, 0) 

carrot_8 = GameSprite("plant_seed.png", ogorod_8.rect.x, ogorod_8.rect.y, 70, 100, 0) 

carrot_9 = GameSprite("plant_seed.png", ogorod_9.rect.x, ogorod_9.rect.y, 70, 100, 0) 

carrot_10 = GameSprite("plant_seed.png", ogorod_10.rect.x, ogorod_10.rect.y, 70, 100, 0) 

carrot_11 = GameSprite("plant_seed.png", ogorod_11.rect.x, ogorod_11.rect.y, 70, 100, 0) 

carrot_12 = GameSprite("plant_seed.png", ogorod_12.rect.x, ogorod_12.rect.y, 70, 100, 0) 

potato_1 = GameSprite("plant_seed.png", ogorod_1.rect.x, ogorod_1.rect.y, 70 , 100, 0) 

potato_2 = GameSprite("plant_seed.png", ogorod_2.rect.x, ogorod_2.rect.y, 70 , 100, 0) 

potato_3 = GameSprite("plant_seed.png", ogorod_3.rect.x, ogorod_3.rect.y, 70 , 100, 0) 

potato_4 = GameSprite("plant_seed.png", ogorod_4.rect.x, ogorod_4.rect.y, 70 , 100, 0) 

potato_5 = GameSprite("plant_seed.png", ogorod_5.rect.x, ogorod_5.rect.y, 70 , 100, 0) 

potato_6 = GameSprite("plant_seed.png", ogorod_6.rect.x, ogorod_6.rect.y, 70 , 100, 0) 

potato_7 = GameSprite("plant_seed.png", ogorod_7.rect.x, ogorod_7.rect.y, 70 , 100, 0) 

potato_8 = GameSprite("plant_seed.png", ogorod_8.rect.x, ogorod_8.rect.y, 70 , 100, 0) 

potato_9 = GameSprite("plant_seed.png", ogorod_9.rect.x, ogorod_9.rect.y, 70 , 100, 0) 

potato_10 = GameSprite("plant_seed.png", ogorod_10.rect.x, ogorod_10.rect.y, 70 , 100, 0) 

potato_11 = GameSprite("plant_seed.png", ogorod_11.rect.x, ogorod_11.rect.y, 70 , 100, 0) 

potato_12 = GameSprite("plant_seed.png", ogorod_12.rect.x, ogorod_12.rect.y, 70 , 100, 0) 




def draw_text (text, font, text_col, x, y,):
    img = font.render(text,True,text_col)
    mw.blit(img,(x,y))

list_ogorod = [1,0,0,0,0,0,0,0,0,0,0,0]

def shop_menu():
    global shop_menu_state, shop_menu_img, player, money, tomato_seed, potato_seed, carrot_seed, list_ogorod
    
    while shop_menu_state:
        mw.blit(shop_menu_img,(0,0))
        for e in event.get():   
            if e.type == QUIT:
                shop_menu_state = False   
                player = Player("player.png",300,500,100,100,5)
           
        draw_text("1$", text1,(0,200, 0),230,265)
        draw_text("6$", text1,(0,200, 0),610,265)
        draw_text("3$", text1,(0,200, 0),1000,265)
        draw_text("15$", text1,(0,200, 0),605,500)
                
        if shop_plant_tomato.draw(mw):
            if money >= 1:
                money -= 1
                tomato_seed += 1

        if shop_plant_potato.draw(mw):
            if money >= 6:
                money -= 6
                potato_seed += 1
        
        if shop_plant_carrot.draw(mw):
            if money >= 3:
                money -= 3
                carrot_seed += 1
         
        if ogorod_button_buy.draw(mw):
            ogo = list_ogorod.index(0)
            if ogo < len(list_ogorod):
                if money >= 15:
                    money -= 15
                    list_ogorod[ogo] = 1       
        
        
        if shop_exit.draw(mw):
            shop_menu_state = False
            player = Player("player.png",300,500,100,100,5)
            
        display.update()
        clock.tick(FPS)
        
    shop_menu_state = True
    
def plant_menu():
    global state_plant_10, plant_menu_state, carrot_seed, tomato_seed, potato_seed, state_plant_1, state_plant_2, state_plant_3, state_plant_4, state_plant_5, state_plant_6, state_plant_7, state_plant_8, state_plant_9, state_plant_11, state_plant_12, state_ogorod_1, state_ogorod_2, state_ogorod_3, state_ogorod_4, state_ogorod_5, state_ogorod_6, state_ogorod_7, state_ogorod_8, state_ogorod_9, state_ogorod_10, state_ogorod_11, state_ogorod_12, ogorod_1, ogorod_2, ogorod_3, ogorod_4, ogorod_5, ogorod_6, ogorod_7, ogorod_8, ogorod_9, ogorod_11, ogorod_12
    
    while plant_menu_state:
        for e in event.get():
                
            if e.type == QUIT:
                plant_menu_state = False
                    
        if plant_tomato.draw(mw):
            if tomato_seed >= 1:
                if state_ogorod_1:
                    ogorod_1.planted = True
                    state_plant_1 = 1
                    plants.add(tomato_1)
                    state_ogorod_1 = False
                    
                if state_ogorod_2:
                    ogorod_2.planted = True
                    state_plant_2 = 1
                    plants.add(tomato_2)
                    state_ogorod_2 = False
                    
                if state_ogorod_3:
                    ogorod_3.planted = True
                    state_plant_3 = 1
                    plants.add(tomato_3)
                    state_ogorod_3 = False
                    
                if state_ogorod_4:
                    ogorod_4.planted = True
                    state_plant_4 = 1
                    plants.add(tomato_4)
                    state_ogorod_4 = False
                    
                if state_ogorod_5:
                    ogorod_5.planted = True
                    state_plant_5 = 1
                    plants.add(tomato_5)
                    state_ogorod_5 = False
                    
                if state_ogorod_6:
                    ogorod_6.planted = True
                    state_plant_6 = 1
                    plants.add(tomato_6)
                    state_ogorod_6 = False
                    
                if state_ogorod_7:
                    ogorod_7.planted = True
                    state_plant_7 = 1
                    plants.add(tomato_7)
                    state_ogorod_7 = False
                    
                if state_ogorod_8:
                    ogorod_8.planted = True
                    state_plant_8 = 1
                    plants.add(tomato_8)
                    state_ogorod_8 = False
                    
                if state_ogorod_9:
                    ogorod_9.planted = True
                    state_plant_9 = 1
                    plants.add(tomato_9)
                    state_ogorod_9 = False
                    
                if state_ogorod_10:
                    ogorod_10.planted = True
                    state_plant_10 = 1
                    plants.add(tomato_10)
                    state_ogorod_10 = False
                    
                if state_ogorod_11:
                    ogorod_11.planted = True
                    state_plant_11 = 1
                    plants.add(tomato_11)
                    state_ogorod_11 = False
                    
                if state_ogorod_12:
                    ogorod_12.planted = True
                    state_plant_12 = 1
                    plants.add(tomato_12)
                    state_ogorod_12 = False
                    
                plant_menu_state = False
                tomato_seed -= 1
                
            else:
                draw_text("У вас закінчилося насіння купіть у магазині", text5, (200,0,0), 50, 200)
        
        
        
        
                
        if plant_carrot.draw(mw):
            if carrot_seed >= 1:

                if state_ogorod_1:
                    ogorod_1.planted = True
                    state_plant_1 = 2
                    plants.add(carrot_1)
                    state_ogorod_1 = False
                    
                if state_ogorod_2:
                    ogorod_2.planted = True
                    state_plant_2 = 2
                    plants.add(carrot_2)
                    state_ogorod_2 = False
                    
                if state_ogorod_3:
                    ogorod_3.planted = True
                    state_plant_3 = 2
                    plants.add(carrot_3)
                state_ogorod_3 = False
                    
                if state_ogorod_4:
                    ogorod_4.planted = True
                    state_plant_4 = 2
                    plants.add(carrot_4)
                    state_ogorod_4 = False
                    
                if state_ogorod_5:
                    ogorod_5.planted = True
                    state_plant_5 = 2
                    plants.add(carrot_5)
                    state_ogorod_5 = False
                    
                if state_ogorod_6:
                    ogorod_6.planted = True
                    state_plant_6 = 2
                    plants.add(carrot_6)
                    state_ogorod_6 = False
                    
                if state_ogorod_7:
                    ogorod_7.planted = True
                    state_plant_7 = 2
                    plants.add(carrot_7)
                    state_ogorod_7 = False
                    
                if state_ogorod_8:
                    ogorod_8.planted = True
                    state_plant_8 = 2
                    plants.add(carrot_8)
                    state_ogorod_8 = False
                    
                if state_ogorod_9:
                    ogorod_9.planted = True
                    state_plant_9 = 2
                    plants.add(carrot_9)
                    state_ogorod_9 = False
                    
                if state_ogorod_10:
                    ogorod_10.planted = True
                    state_plant_10 = 2
                    plants.add(carrot_10)
                    state_ogorod_10 = False
                    
                if state_ogorod_11:
                    ogorod_11.planted = True
                    state_plant_11 = 2
                    plants.add(carrot_11)
                    state_ogorod_11 = False
                    
                if state_ogorod_12:
                    ogorod_12.planted = True
                    state_plant_12 = 2
                    plants.add(carrot_12)
                    state_ogorod_12 = False
                    
                plant_menu_state = False
                carrot_seed -= 1
            else:
                draw_text("У вас закінчилося насіння купіть у магазині", text5, (200,0,0), 50, 200)
        
        if plant_potato.draw(mw):
            if potato_seed >= 1:

                if state_ogorod_1:
                    ogorod_1.planted = True
                    state_plant_1 = 3
                    plants.add(potato_1)                 
                    state_ogorod_1 = False
                    
                if state_ogorod_2:
                    ogorod_2.planted = True
                    state_plant_2 = 3
                    plants.add(potato_2)                 
                    state_ogorod_2 = False
                    
                if state_ogorod_3:
                    ogorod_3.planted = True
                    state_plant_3 = 3
                    plants.add(potato_3)                 
                    state_ogorod_3 = False
                    
                if state_ogorod_4:
                    ogorod_4.planted = True
                    state_plant_4 = 3
                    plants.add(potato_4)                 
                    state_ogorod_4 = False
                    
                if state_ogorod_5:
                    ogorod_5.planted = True
                    state_plant_5 = 3
                    plants.add(potato_5)                 
                    state_ogorod_5 = False
                    
                if state_ogorod_6:
                    ogorod_6.planted = True
                    state_plant_6 = 3
                    plants.add(potato_6)                 
                    state_ogorod_6 = False
                    
                if state_ogorod_7:
                    ogorod_7.planted = True
                    state_plant_7 = 3
                    plants.add(potato_7)                 
                    state_ogorod_7 = False
                    
                if state_ogorod_8:
                    ogorod_8.planted = True
                    state_plant_8 = 3
                    plants.add(potato_8)                 
                    state_ogorod_8 = False
                    
                if state_ogorod_9:
                    ogorod_9.planted = True
                    state_plant_9 = 3
                    plants.add(potato_9)                 
                    state_ogorod_9 = False
                    
                if state_ogorod_10:
                    ogorod_10.planted = True
                    state_plant_10 = 3
                    plants.add(potato_10)                 
                    state_ogorod_10 = False
                    
                if state_ogorod_11:
                    ogorod_11.planted = True 
                    state_plant_11 = 3
                    plants.add(potato_11)                 
                    state_ogorod_11 = False
                    
                if state_ogorod_12:
                    ogorod_12.planted = True
                    state_plant_12 = 3
                    plants.add(potato_12)                 
                    state_ogorod_12 = False
                    
                plant_menu_state = False   
                potato_seed -= 1
                
            else:
                draw_text("У вас закінчилося насіння купіть y магазині", text5, (200,0,0), 50, 200)
        if back_button_plant.draw(mw):
            plant_menu_state = False
                     
        display.update()
        clock.tick(FPS)
        
def menu():
    global game_paused, menu_state, state_menu, game
    while state_menu:
        
        mw.blit(map,(0,0))
        if game_paused:
            
            if menu_state == "main":
            
                draw_text("TRY YOURSELF AS FARMER!",text2,text_col,50,152)
                draw_text("TRY YOURSELF AS FARMER!",text2,(200, 1, 1),52,150)
                if play_button.draw(mw):
                    game = True
                    start_the_game()

                if settings_button.draw(mw):
                    menu_state = "options"

                if exit_button.draw(mw):
                    sys.exit()

            if menu_state == "options":
                if volume_button.draw(mw):
                    menu_state = "volume"

                if back_button.draw(mw):
                    menu_state = "main"

            if menu_state == "volume":
                if volume1_button.draw(mw):
                    mixer.music.set_volume(0)

                if volume2_button.draw(mw):
                    mixer.music.set_volume(0.25)

                if volume3_button.draw(mw):
                    mixer.music.set_volume(0.5)

                if volume4_button.draw(mw):
                    mixer.music.set_volume(1)

                if back_button.draw(mw):
                    menu_state = "options"
                
        else:
            draw_text("Press spase to go the menu",text1,text_col,160,250)
            keys = key.get_pressed()
            if keys[K_SPACE]:
                game_paused = True
        
        for e in event.get():
            if e.type == QUIT:
                sys.exit()

        display.update()
        clock.tick(FPS)

def start_the_game():
    global coin_1, coin_2, coin_3, coin_4, coin_5, coin_6, coin_7, coin_8, coin_9, coin_10, coin_11, coin_12, now_time_1, now_time_2, now_time_3, now_time_4, now_time_5, now_time_6, now_time_7, now_time_8, now_time_9, now_time_10, now_time_11, now_time_12, plant_1_img, plant_2_img, plant_3_img, plant_4_img, plant_5_img, plant_6_img, plant_7_img, plant_8_img, plant_9_img, plant_10_img, plant_11_img, plant_12_img, state_ogorod_1, state_ogorod_2, state_ogorod_3, state_ogorod_4, state_ogorod_5, state_ogorod_6, state_ogorod_7, state_ogorod_8, state_ogorod_9, state_ogorod_10, state_ogorod_11, state_ogorod_12, state_plant_1, state_plant_2, state_plant_3, state_plant_4, state_plant_5, state_plant_6, state_plant_7, state_plant_8, state_plant_9, state_plant_10, state_plant_11, state_plant_12, tomato_1, tomato_2, tomato_3, tomato_4, tomato_5, tomato_6, tomato_7, tomato_8, tomato_9, tomato_10, tomato_11, tomato_12, pick_button, now_time, money, state_menu, invertar, plant_seed_1, plant_seed_2, plant_seed_3, plant_seed_4, plant_seed_5, plant_seed_6, plant_seed_7, plant_seed_8, plant_seed_9, plant_seed_10, plant_seed_11, plant_seed_12, state_coin_1, state_coin_2, state_coin_3, state_coin_4, state_coin_5, state_coin_6, state_coin_7, state_coin_8, state_coin_9, state_coin_10, state_coin_11, state_coin_12, coin, state_plant_1, state_plant_2, state_plant_3,state_plant_4 ,state_plant_5, state_plant_6, state_plant_7, state_plant_8, state_plant_9, state_plant_10, state_plant_11, state_plant_12, game, plant_menu_state, potato_1, potato_2, potato_3, potato_4, potato_5, potato_6, potato_7, potato_8, potato_9, potato_10, potato_11, potato_12, carrot_1, carrot_2, carrot_3, carrot_4, carrot_5, carrot_6, carrot_7, carrot_8, carrot_9, carrot_10, carrot_11, carrot_12, x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, x_10, x_11, x_12, y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8, y_9, y_10, y_11, y_12

    while game:
        
        for e in event.get(): 
            if e.type == QUIT:
                game = False

        if not finish:
            mw.blit(map,(0,0)) 
            pick_button = Button(player.rect.x,player.rect.y - 150,pick_img,1)
            ogorod_1.update()
            ogorod_1.reset()
            ogorod_2.update()
            ogorod_2.reset()            
            ogorod_3.update()
            ogorod_3.reset()
            ogorod_4.update()
            ogorod_4.reset()
            ogorod_5.update()
            ogorod_5.reset()
            ogorod_6.update()
            ogorod_6.reset()
            ogorod_7.update()
            ogorod_7.reset()
            ogorod_8.update()
            ogorod_8.reset()
            ogorod_9.update()
            ogorod_9.reset()
            ogorod_10.update()
            ogorod_10.reset()
            ogorod_11.update()
            ogorod_11.reset()
            ogorod_12.update()
            ogorod_12.reset()
            plants.draw(mw)
            plants.update()
            coins.draw(mw)
            coins.update()
            shop.update()
            shop.reset()
            player.update()
            player.reset()
            mw.blit(money_img, (376, 15))
            mw.blit(invertar,(22,16))
            mw.blit(invertar,(144,16))
            mw.blit(invertar,(266,16))
            mw.blit(tomato_seed_img,(22,16))
            mw.blit(potato_seed_img,(144,16))
            mw.blit(carrot_seed_img,(266,16))
            draw_text(str(tomato_seed),text4,(39, 15, 144), 30, 112)
            draw_text(str(potato_seed),text4,(39, 15, 144), 152, 112)
            draw_text(str(carrot_seed),text4,(39, 15, 144), 274, 112)
            draw_text(str(money),text4,(30, 235, 0), 436, 36)
            
            if sprite.collide_rect(ogorod_1,player) and list_ogorod[0]:
                plant_button = Button(player.rect.x + 100,player.rect.y - 100,plant_1_img,1)
                pick_button = Button(player.rect.x - 100,player.rect.y + 100,pick_img,1)
                if plant_button.draw(mw):
                    if state_coin_1 == 0:
                        state_ogorod_1 = True
                        plant_menu_state = True    
                        plant_menu()
                
            if sprite.collide_rect(ogorod_2,player) and list_ogorod[1]:
                plant_button = Button(player.rect.x - 100,player.rect.y - 100,plant_2_img,1)
                pick_button = Button(player.rect.x - 100,player.rect.y + 100,pick_img,1)
                if plant_button.draw(mw):
                    if state_coin_2 == 0:
                        state_ogorod_2 = True
                        plant_menu_state = True
                        plant_menu()
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)
                
            if sprite.collide_rect(ogorod_3,player) and list_ogorod[2]:
                plant_button = Button(player.rect.x + 100,player.rect.y + 100,plant_3_img,1)
                pick_button = Button(player.rect.x - 100,player.rect.y + 100,pick_img,1)
                if plant_button.draw(mw):
                    if state_coin_3 == 0:
                        state_ogorod_3 = True
                        plant_menu_state = True
                        plant_menu()
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)
                
            if sprite.collide_rect(ogorod_4,player) and list_ogorod[3]:
                plant_button = Button(player.rect.x - 100,player.rect.y + 100,plant_4_img,1)
                pick_button = Button(player.rect.x - 100,player.rect.y + 100,pick_img,1)
                if plant_button.draw(mw):
                    if state_coin_4 == 0:
                        state_ogorod_4 = True
                        plant_menu_state = True
                        plant_menu()
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)
                
            if sprite.collide_rect(ogorod_5,player) and list_ogorod[4]:
                plant_button = Button(player.rect.x + 100,player.rect.y - 100,plant_5_img,1)
                if plant_button.draw(mw):
                    if state_coin_5 == 0:
                        state_ogorod_5 = True
                        plant_menu_state = True
                        plant_menu()
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)
                
            if sprite.collide_rect(ogorod_6,player) and list_ogorod[5]:
                plant_button = Button(player.rect.x - 100,player.rect.y - 100,plant_6_img,1)
                if plant_button.draw(mw):
                    if state_coin_6 == 0:
                        state_ogorod_6 = True
                        plant_menu_state = True
                        plant_menu()
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)
                
            if sprite.collide_rect(player,ogorod_7) and list_ogorod[6]:
                plant_button = Button(player.rect.x + 100,player.rect.y + 100,plant_7_img,1)
                if plant_button.draw(mw):
                    if state_coin_7 == 0:
                        state_ogorod_7 = True
                        plant_menu_state = True
                        plant_menu()
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)
                
            if sprite.collide_rect(ogorod_8,player) and list_ogorod[7]:
                plant_button = Button(player.rect.x - 100,player.rect.y + 100,plant_8_img,1)
                if plant_button.draw(mw):
                    if state_coin_8 == 0:
                        state_ogorod_8 = True
                        plant_menu_state = True
                        plant_menu()
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)
                
            if sprite.collide_rect(ogorod_9,player) and list_ogorod[8]:
                plant_button = Button(player.rect.x + 100,player.rect.y - 100,plant_9_img,1)
                if plant_button.draw(mw):
                    if state_coin_9 == 0:
                        state_ogorod_9 = True
                        plant_menu_state = True
                        plant_menu()
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)
                
            if sprite.collide_rect(ogorod_10,player) and list_ogorod[9]:
                plant_button = Button(player.rect.x - 100,player.rect.y - 100,plant_10_img,1)
                if plant_button.draw(mw):
                    if state_coin_10 == 0:
                        plant_menu_state = True
                        state_ogorod_10 = True
                        plant_menu()
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)
                
            if sprite.collide_rect(ogorod_11,player) and list_ogorod[10]:
                plant_button = Button(player.rect.x + 100,player.rect.y + 100,plant_11_img,1)              
                if plant_button.draw(mw):
                    if state_coin_11 == 0:
                        state_ogorod_11 = True
                        plant_menu_state = True
                        plant_menu()
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)
                
            if sprite.collide_rect(ogorod_12,player) and list_ogorod[11]:
                plant_button = Button(player.rect.x - 100,player.rect.y + 100,plant_12_img,1)             
                if plant_button.draw(mw):
                    if state_coin_12 == 0:
                        state_ogorod_12 = True
                        plant_menu_state = True
                        plant_menu()
                        
                    else:
                        draw_text("Вам треба зібрати монетку щоб посадити",text3,(200, 0, 0), 50, 340)

            if plant_seed_1:
                if not ogorod_1.planted: 
                    if pick_button.draw(mw):
                        if state_plant_1 == 1:
                            tomato_1.kill()
                            tomato_1 = GameSprite("plant_seed.png", ogorod_1.rect.x + 10 , ogorod_1.rect.y, 70, 100 , 0) 
                        
                        if state_plant_1 == 2:
                            carrot_1.kill()
                            carrot_1 = GameSprite("plant_seed.png", ogorod_1.rect.x + 10 , ogorod_1.rect.y, 70, 100 , 0)                  

                        if state_plant_1 == 3:
                            potato_1.kill()
                            potato_1 = GameSprite("plant_seed.png", ogorod_1.rect.x + 10 , ogorod_1.rect.y, 70, 100 , 0) 
                        
                        coin_1 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_1)
                        state_coin_1 = 1
                        plant_seed_1 = False
                        
            if plant_seed_2:
                if not ogorod_2.planted: 
                    if pick_button.draw(mw):
                        if state_plant_2 == 1:
                            tomato_2.kill()
                            tomato_2 = GameSprite("plant_seed.png", ogorod_2.rect.x + 10 , ogorod_2.rect.y, 70, 100 , 0) 
                        
                        if state_plant_2 == 2:
                            carrot_2.kill()   
                            carrot_2 = GameSprite("plant_seed.png", ogorod_2.rect.x + 10 , ogorod_2.rect.y, 70, 100 , 0)                  

                        if state_plant_2 == 3:
                            potato_2.kill()
                            potato_2 = GameSprite("plant_seed.png", ogorod_2.rect.x + 10 , ogorod_2.rect.y, 70, 100 , 0) 
                       
                        coin_2 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_2)
                        state_coin_2 = 1
                        plant_seed_2 = False

            if plant_seed_3:
                if not ogorod_3.planted: 
                    if pick_button.draw(mw):
                        if state_plant_3 == 1:
                            tomato_3.kill()
                            tomato_3 = GameSprite("plant_seed.png", ogorod_3.rect.x + 10 , ogorod_3.rect.y, 70, 100 , 0) 
                        
                        if state_plant_3 == 2:
                            carrot_3.kill()   
                            carrot_3 = GameSprite("plant_seed.png", ogorod_3.rect.x + 10 , ogorod_3.rect.y, 70, 100 , 0)                  

                        if state_plant_3 == 3:
                            potato_3.kill()
                            potato_3 = GameSprite("plant_seed.png", ogorod_3.rect.x + 10 , ogorod_3.rect.y, 70, 100 , 0) 
                       
                        coin_3 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_3)
                        state_coin_3 = 1
                        plant_seed_3 = False

            if plant_seed_4:
                if not ogorod_4.planted: 
                    if pick_button.draw(mw):
                        if state_plant_4 == 1:
                            tomato_4.kill()
                            tomato_4 = GameSprite("plant_seed.png", ogorod_4.rect.x + 10 , ogorod_4.rect.y, 70, 100 , 0) 
                        
                        if state_plant_4 == 2:
                            carrot_4.kill()   
                            carrot_4 = GameSprite("plant_seed.png", ogorod_4.rect.x + 10 , ogorod_4.rect.y, 70, 100 , 0)                  

                        if state_plant_4 == 3:
                            potato_4.kill()
                            potato_4 = GameSprite("plant_seed.png", ogorod_4.rect.x + 10 , ogorod_4.rect.y, 70, 100 , 0) 
                       
                        coin_4 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_4)
                        state_coin_4 = 1
                        plant_seed_4 = False
                        
            if plant_seed_5:
                if not ogorod_5.planted: 
                    if pick_button.draw(mw):
                        if state_plant_5 == 1:
                            tomato_5.kill()
                            tomato_5 = GameSprite("plant_seed.png", ogorod_5.rect.x + 10 , ogorod_5.rect.y, 70, 100 , 0) 
                        
                        if state_plant_5 == 2:
                            carrot_5.kill()   
                            carrot_5 = GameSprite("plant_seed.png", ogorod_5.rect.x + 10 , ogorod_5.rect.y, 70, 100 , 0)                  

                        if state_plant_5 == 3:
                            potato_5.kill()
                            potato_5 = GameSprite("plant_seed.png", ogorod_5.rect.x + 10 , ogorod_5.rect.y, 70, 100 , 0) 
                       
                        coin_5 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_5)
                        state_coin_5 = 1
                        plant_seed_5 = False

            if plant_seed_6:
                if not ogorod_6.planted: 
                    if pick_button.draw(mw):
                        if state_plant_6 == 1:
                            tomato_6.kill()
                            tomato_6 = GameSprite("plant_seed.png", ogorod_6.rect.x + 10 , ogorod_6.rect.y, 70, 100 , 0) 
                        
                        if state_plant_6 == 2:
                            carrot_6.kill()   
                            carrot_6 = GameSprite("plant_seed.png", ogorod_6.rect.x + 10 , ogorod_6.rect.y, 70, 100 , 0)                  

                        if state_plant_6 == 3:
                            potato_6.kill()
                            potato_6 = GameSprite("plant_seed.png", ogorod_6.rect.x + 10 , ogorod_6.rect.y, 70, 100 , 0) 
                        coin_6 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_6)
                        state_coin_6 = 1
                        plant_seed_6 = False

            if plant_seed_7:
                if not ogorod_7.planted:
                    if pick_button.draw(mw):
                        if state_plant_7 == 1:
                            tomato_7.kill()
                            tomato_7 = GameSprite("plant_seed.png", ogorod_7.rect.x + 10 , ogorod_7.rect.y, 70, 100 , 0) 
                        
                        if state_plant_7 == 2:
                            carrot_7.kill()   
                            carrot_7 = GameSprite("plant_seed.png", ogorod_7.rect.x + 10 , ogorod_7.rect.y, 70, 100 , 0)                  

                        if state_plant_7 == 3:
                            potato_7.kill()
                            potato_7 = GameSprite("plant_seed.png", ogorod_7.rect.x + 10 , ogorod_7.rect.y, 70, 100 , 0) 
                        coin_7 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_7)
                        state_coin_7 = 1
                        plant_seed_7 = False
                        
            if plant_seed_8:
                if not ogorod_8.planted: 
                    if pick_button.draw(mw):
                        if state_plant_8 == 1:
                            tomato_8.kill()
                            tomato_8 = GameSprite("plant_seed.png", ogorod_8.rect.x + 10 , ogorod_8.rect.y, 70, 100 , 0) 
                        
                        if state_plant_8 == 2:
                            carrot_8.kill()   
                            carrot_8 = GameSprite("plant_seed.png", ogorod_8.rect.x + 10 , ogorod_8.rect.y, 70, 100 , 0)                  

                        if state_plant_8 == 3:
                            potato_8.kill()
                            potato_8 = GameSprite("plant_seed.png", ogorod_8.rect.x + 10 , ogorod_8.rect.y, 70, 100 , 0) 
                        coin_8 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_8)
                        state_coin_8 = 1
                        plant_seed_8 = False
                        
            if plant_seed_9:
                if not ogorod_9.planted: 
                    if pick_button.draw(mw):
                        if state_plant_9 == 1:
                            tomato_9.kill()
                            tomato_9 = GameSprite("plant_seed.png", ogorod_9.rect.x + 10 , ogorod_9.rect.y, 70, 100 , 0) 
                        
                        if state_plant_9 == 2:
                            carrot_9.kill()   
                            carrot_9 = GameSprite("plant_seed.png", ogorod_9.rect.x + 10 , ogorod_9.rect.y, 70, 100 , 0)                  

                        if state_plant_9 == 3:
                            potato_9.kill()
                            potato_9 = GameSprite("plant_seed.png", ogorod_9.rect.x + 10 , ogorod_9.rect.y, 70, 100 , 0) 
                        coin_9 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_9)
                        state_coin_9 = 1
                        plant_seed_9 = False
                        
            if plant_seed_10:
                if not ogorod_10.planted: 
                    if pick_button.draw(mw):
                        if state_plant_10 == 1:
                            tomato_10.kill()
                            tomato_10 = GameSprite("plant_seed.png", ogorod_10.rect.x + 10 , ogorod_10.rect.y, 70, 100 , 0) 
                        
                        if state_plant_1 == 2:
                            carrot_1.kill()   
                            carrot_1 = GameSprite("plant_seed.png", ogorod_10.rect.x + 10 , ogorod_10.rect.y, 70, 100 , 0)                  

                        if state_plant_10 == 3:
                            potato_10.kill()
                            potato_10 = GameSprite("plant_seed.png", ogorod_10.rect.x + 10 , ogorod_10.rect.y, 70, 100 , 0) 
                        coin_10 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_10)
                        state_coin_10 = 1
                        plant_seed_10 = False

            if plant_seed_11:
                if not ogorod_11.planted: 
                    if pick_button.draw(mw):
                        if state_plant_11 == 1:
                            tomato_11.kill()
                            tomato_11 = GameSprite("plant_seed.png", ogorod_11.rect.x + 10 , ogorod_11.rect.y, 70, 100 , 0) 
                        
                        if state_plant_11 == 2:
                            carrot_11.kill()   
                            carrot_11 = GameSprite("plant_seed.png", ogorod_11.rect.x + 10 , ogorod_11.rect.y, 70, 100 , 0)                  

                        if state_plant_11 == 3:
                            potato_11.kill()
                            potato_11 = GameSprite("plant_seed.png", ogorod_11.rect.x + 10 , ogorod_11.rect.y, 70, 100 , 0) 
                        coin_11 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_11)
                        state_coin_11 = 1
                        plant_seed_11 = False

            if plant_seed_12:
                if not ogorod_12.planted: 
                    if pick_button.draw(mw):
                        if state_plant_12 == 1:
                            tomato_12.kill()
                            tomato_12 = GameSprite("plant_seed.png", ogorod_12.rect.x + 10 , ogorod_12.rect.y, 70, 100 , 0) 
                        
                        if state_plant_12 == 2:
                            carrot_12.kill()   
                            carrot_12 = GameSprite("plant_seed.png", ogorod_12.rect.x + 10 , ogorod_12.rect.y, 70, 100 , 0)                  

                        if state_plant_12 == 3:
                            potato_12.kill()
                            potato_12 = GameSprite("plant_seed.png", ogorod_12.rect.x + 10 , ogorod_12.rect.y, 70, 100 , 0) 

                        coin_12 = GameSprite('coin.png', randint(350,900), randint(150,600), 100, 100, 1)
                        coins.add(coin_12)
                        state_coin_12 = 1
                        plant_seed_12 = False

            if sprite.collide_rect(shop,player):
                shop_menu()
                
            if ogorod_1.planted:
                now_time_1 -= 1
                    
                if  now_time_1 <= 0:
                    if state_plant_1 == 1:
                        tomato_1.kill()
                        tomato_1 = GameSprite("tomato.png", ogorod_1.rect.x , ogorod_1.rect.y, 100, 100, 0)
                        plants.add(tomato_1)
                    
                    if state_plant_1 == 2:
                        carrot_1.kill()
                        carrot_1 = GameSprite("carrot.png", ogorod_1.rect.x, ogorod_1.rect.y, 100, 100, 0)
                        plants.add(carrot_1)                    
                    
                    if state_plant_1 == 3:
                        potato_1.kill()
                        potato_1 = GameSprite("potato.png", ogorod_1.rect.x, ogorod_1.rect.y, 100, 100, 0)
                        plants.add(potato_1)                    
                    
                    now_time_1 = 300
                    plant_seed_1 = True
                    ogorod_1.planted = False
                    
            if ogorod_2.planted:
                now_time_2 -= 1
                    
                if  now_time_2 <= 0:
                    if state_plant_2 == 1:
                        tomato_2.kill()
                        tomato_2 = GameSprite("tomato.png", ogorod_2.rect.x, ogorod_2.rect.y, 100, 100, 0)
                        plants.add(tomato_2)
                    
                    if state_plant_2 == 2:
                        carrot_2.kill()
                        carrot_2 = GameSprite("carrot.png", ogorod_2.rect.x, ogorod_2.rect.y, 100, 100, 0)
                        plants.add(carrot_2)                    
                    
                    if state_plant_2 == 3:
                        potato_2.kill()
                        potato_2 = GameSprite("potato.png", ogorod_2.rect.x, ogorod_2.rect.y, 100, 100, 0)
                        plants.add(potato_2)                    
                    
                    now_time_2 = 300
                    plant_seed_2 = True
                    ogorod_2.planted = False                    
                    
            if ogorod_3.planted:
                now_time_3 -= 1
                    
                if  now_time_3 <= 0:
                    if state_plant_3 == 1:
                        tomato_3.kill()
                        tomato_3 = GameSprite("tomato.png", ogorod_3.rect.x , ogorod_3.rect.y, 100, 100, 0)
                        plants.add(tomato_3)
                    
                    if state_plant_3 == 2:
                        carrot_3.kill()
                        carrot_3 = GameSprite("carrot.png", ogorod_3.rect.x, ogorod_3.rect.y, 100, 100, 0)
                        plants.add(carrot_3)                    
                    
                    if state_plant_3 == 3:
                        potato_3.kill()
                        potato_3 = GameSprite("potato.png", ogorod_3.rect.x, ogorod_3.rect.y, 100, 100, 0)
                        plants.add(potato_3)                    
                    
                    now_time_3 = 300
                    plant_seed_3 = True
                    ogorod_3.planted = False      
                    
            if ogorod_4.planted:
                now_time_4 -= 1
                    
                if  now_time_4 <= 0:
                    if state_plant_4 == 1:
                        tomato_4.kill()
                        tomato_4 = GameSprite("tomato.png", ogorod_4.rect.x, ogorod_4.rect.y, 100, 100, 0)
                        plants.add(tomato_4)
                    
                    if state_plant_4 == 2:
                        carrot_4.kill()
                        carrot_4 = GameSprite("carrot.png", ogorod_4.rect.x, ogorod_4.rect.y, 100, 100, 0)
                        plants.add(carrot_4)                    
                    
                    if state_plant_4 == 3:
                        potato_4.kill()
                        potato_4 = GameSprite("potato.png", ogorod_4.rect.x, ogorod_4.rect.y, 100, 100, 0)
                        plants.add(potato_4)                    
                    
                    now_time_4 = 300
                    plant_seed_4 = True
                    ogorod_4.planted = False      
                    
            if ogorod_5.planted:
                now_time_5 -= 1
                
                if  now_time_5 <= 0:
                    if state_plant_5 == 1:
                        tomato_5.kill()
                        tomato_5 = GameSprite("tomato.png", ogorod_5.rect.x, ogorod_5.rect.y, 100, 100, 0)
                        plants.add(tomato_5)
                    
                    if state_plant_5 == 2:
                        carrot_5.kill()
                        carrot_5 = GameSprite("carrot.png", ogorod_5.rect.x, ogorod_5.rect.y, 100, 100, 0)
                        plants.add(carrot_5)                    
                    
                    if state_plant_5 == 3:
                        potato_5.kill()
                        potato_5 = GameSprite("potato.png", ogorod_5.rect.x, ogorod_5.rect.y, 100, 100, 0)
                        plants.add(potato_5)                    
                    
                    now_time_5 = 300
                    plant_seed_5 = True
                    ogorod_5.planted = False      
                    
            if ogorod_6.planted:
                now_time_6 -= 1
                    
                if  now_time_6 <= 0:
                    if state_plant_6 == 1:
                        tomato_6.kill()
                        tomato_6 = GameSprite("tomato.png", ogorod_6.rect.x, ogorod_6.rect.y, 100, 100, 0)
                        plants.add(tomato_6)
                    
                    if state_plant_6 == 2:
                        carrot_6.kill()
                        carrot_6 = GameSprite("carrot.png", ogorod_6.rect.x, ogorod_6.rect.y, 100, 100, 0)
                        plants.add(carrot_6)                    
                    
                    if state_plant_6 == 3:
                        potato_6.kill()
                        potato_6 = GameSprite("potato.png", ogorod_6.rect.x, ogorod_6.rect.y, 100, 100, 0)
                        plants.add(potato_6)                    
                    
                    now_time_6 = 300
                    plant_seed_6 = True
                    ogorod_6.planted = False      
                    
            if ogorod_7.planted:
                now_time_7 -= 1
                    
                if  now_time_7 <= 0:
                    if state_plant_7 == 1:
                        tomato_7.kill()
                        tomato_7 = GameSprite("tomato.png", ogorod_7.rect.x, ogorod_7.rect.y, 100, 100, 0)
                        plants.add(tomato_7)
                    
                    if state_plant_7 == 2:
                        carrot_7.kill()
                        carrot_7 = GameSprite("carrot.png", ogorod_7.rect.x, ogorod_7.rect.y, 100, 100, 0)
                        plants.add(carrot_7)                    
                    
                    if state_plant_7 == 3:
                        potato_7.kill()
                        potato_7 = GameSprite("potato.png", ogorod_7.rect.x, ogorod_7.rect.y, 100, 100, 0)
                        plants.add(potato_7)                    
                    
                    now_time_7 = 300
                    plant_seed_7 = True
                    ogorod_7.planted = False      
                    
            if ogorod_8.planted:
                now_time_8 -= 1
                    
                if  now_time_8 <= 0:
                    if state_plant_8 == 1:
                        tomato_8.kill()
                        tomato_8 = GameSprite("tomato.png", ogorod_8.rect.x, ogorod_8.rect.y, 100, 100, 0)
                        plants.add(tomato_8)
                    
                    if state_plant_8 == 2:
                        carrot_8.kill()
                        carrot_8 = GameSprite("carrot.png", ogorod_8.rect.x, ogorod_8.rect.y, 100, 100, 0)
                        plants.add(carrot_8)                    
                    
                    if state_plant_8 == 3:
                        potato_8.kill()
                        potato_8 = GameSprite("potato.png", ogorod_8.rect.x, ogorod_8.rect.y, 100, 100, 0)
                        plants.add(potato_8)                    
                    
                    now_time_8 = 300
                    plant_seed_8 = True
                    ogorod_8.planted = False      
                    
            if ogorod_9.planted:
                now_time_9 -= 1
                    
                if  now_time_9 <= 0:
                    if state_plant_9 == 1:
                        tomato_9.kill()
                        tomato_9 = GameSprite("tomato.png", ogorod_9.rect.x, ogorod_9.rect.y, 100, 100, 0)
                        plants.add(tomato_9)
                    
                    if state_plant_9 == 2:
                        carrot_9.kill()
                        carrot_9 = GameSprite("carrot.png", ogorod_9.rect.x, ogorod_9.rect.y, 100, 100, 0)
                        plants.add(carrot_9)                    
                    
                    if state_plant_9 == 3:
                        potato_9.kill()
                        potato_9 = GameSprite("potato.png", ogorod_9.rect.x, ogorod_9.rect.y, 100, 100, 0)
                        plants.add(potato_9)                    
                    
                    now_time_9 = 300
                    plant_seed_9 = True
                    ogorod_9.planted = False      
                    
            if ogorod_10.planted:
                now_time_10 -= 1
                    
                if  now_time_10 <= 0:
                    if state_plant_10 == 1:
                        tomato_10.kill()
                        tomato_10 = GameSprite("tomato.png", ogorod_10.rect.x, ogorod_10.rect.y, 100, 100, 0)
                        plants.add(tomato_10)
                    
                    if state_plant_10 == 2:
                        carrot_10.kill()
                        carrot_10 = GameSprite("carrot.png", ogorod_10.rect.x, ogorod_10.rect.y, 100, 100, 0)
                        plants.add(carrot_10)                    
                    
                    if state_plant_10 == 3:
                        potato_10.kill()
                        potato_10 = GameSprite("potato.png", ogorod_10.rect.x, ogorod_10.rect.y, 100, 100, 0)
                        plants.add(potato_10)                    
                    
                    now_time_10 = 300
                    plant_seed_10 = True
                    ogorod_10.planted = False      
                    
            if ogorod_11.planted:
                now_time_11 -= 1
                    
                if  now_time_11 <= 0:
                    if state_plant_11 == 1:
                        tomato_11.kill()
                        tomato_11 = GameSprite("tomato.png", ogorod_11.rect.x, ogorod_11.rect.y, 100, 100, 0)
                        plants.add(tomato_11)
                    
                    if state_plant_11 == 2:
                        carrot_11.kill()
                        carrot_11 = GameSprite("carrot.png", ogorod_11.rect.x, ogorod_11.rect.y, 100, 100, 0)
                        plants.add(carrot_11)                    
                    
                    if state_plant_11 == 3:
                        potato_11.kill()
                        potato_11 = GameSprite("potato.png", ogorod_11.rect.x, ogorod_11.rect.y, 100, 100, 0)
                        plants.add(potato_11)                    
                    
                    now_time_11 = 300
                    plant_seed_11 = True
                    ogorod_11.planted = False      
                    
            if ogorod_12.planted:
                now_time_12 -= 1
                    
                if  now_time_12 <= 0:
                    if state_plant_12 == 1:
                        tomato_12.kill()
                        tomato_12 = GameSprite("tomato.png", ogorod_12.rect.x, ogorod_12.rect.y, 100, 100, 0)
                        plants.add(tomato_12)
                    
                    if state_plant_12 == 2:
                        carrot_12.kill()
                        carrot_12 = GameSprite("carrot.png", ogorod_12.rect.x, ogorod_12.rect.y, 100, 100, 0)
                        plants.add(carrot_12)                    
                    
                    if state_plant_12 == 3:
                        potato_12.kill()
                        potato_12 = GameSprite("potato.png", ogorod_12.rect.x, ogorod_12.rect.y, 100, 100, 0)
                        plants.add(potato_12)                    
                    
                    now_time_12 = 300
                    plant_seed_12 = True
                    ogorod_12.planted = False      
             
            if coins.has(coin_1):
                if sprite.collide_rect(coin_1,player):
                    if state_plant_1 == 1:
                        money += 2
                    
                    if state_plant_1 == 2:
                        money += 6
                    
                    if state_plant_1 == 3:
                        money += 11
                        
                    coin_1.kill()
                    state_coin_1 = 0
                    state_plant_1 = 0
                    
            if coins.has(coin_2):
                if sprite.collide_rect(coin_2,player):
                    if state_plant_2 == 1:
                        money += 2
                    
                    if state_plant_2 == 2:
                        money += 6
                    
                    if state_plant_2 == 3:
                        money += 11
                        
                    coin_2.kill()
                    state_coin_2 = 0
                    state_plant_2 = 0
                    
            if coins.has(coin_3):
                if sprite.collide_rect(coin_3,player):
                    if state_plant_3 == 1:
                        money += 2
                    
                    if state_plant_3 == 2:
                        money += 6
                    
                    if state_plant_3 == 3:
                        money += 11
                        
                    coin_3.kill()
                    state_coin_3 = 0
                    state_plant_3 = 0
                    
            if coins.has(coin_4):
                if sprite.collide_rect(coin_4,player):
                    if state_plant_4 == 1:
                        money += 2
                    
                    if state_plant_4 == 2:
                        money += 6
                    
                    if state_plant_4 == 3:
                        money += 11
                        
                    coin_4.kill()
                    state_coin_4 = 0
                    state_plant_4 = 0
                    
            if coins.has(coin_5):
                if sprite.collide_rect(coin_5,player):
                    if state_plant_5 == 1:
                        money += 2
                    
                    if state_plant_5 == 2:
                        money += 6
                    
                    if state_plant_5 == 3:
                        money += 11
                        
                    coin_5.kill()
                    state_coin_5 = 0
                    state_plant_5 = 0
                    
            if coins.has(coin_6):
                if sprite.collide_rect(coin_6,player):
                    if state_plant_6 == 1:
                        money += 2
                    
                    if state_plant_6 == 2:
                        money += 6
                    
                    if state_plant_6 == 3:
                        money += 11
                        
                    coin_6.kill()
                    state_coin_6 = 0
                    state_plant_6 = 0
                    
            if coins.has(coin_7):
                if sprite.collide_rect(coin_7,player):
                    if state_plant_7 == 1:
                        money += 2
                
                    if state_plant_7 == 2:
                        money += 6
                    
                    if state_plant_7 == 3:
                        money += 11
                        
                    coin_7.kill()
                    state_coin_7 = 0
                    state_plant_7 = 0
                    
            if coins.has(coin_8):
                if sprite.collide_rect(coin_8,player):
                    if state_plant_8 == 1:
                        money += 2
                    
                    if state_plant_8 == 2:
                        money += 6
                    
                    if state_plant_8 == 3:
                        money += 11
                        
                    coin_8.kill()
                    state_coin_8 = 0
                    state_plant_8 = 0
                    
            if coins.has(coin_9):
                if sprite.collide_rect(coin_9,player):
                    if state_plant_9 == 1:
                        money += 2
                    
                    if state_plant_9 == 2:
                        money += 6
                    
                    if state_plant_9 == 3:
                        money += 11
                        
                    coin_9.kill()
                    state_coin_9 = 0
                    state_plant_9 = 0
                    
            if coins.has(coin_10):
                if sprite.collide_rect(coin_10,player):
                    if state_plant_10 == 1:
                        money += 2
                    
                    if state_plant_10 == 2:
                        money += 6
                    
                    if state_plant_10 == 3:
                        money += 6
                    coin_10.kill()
                    state_coin_10 = 0
                    state_plant_10 = 0
                    
            if coins.has(coin_11):
                if sprite.collide_rect(coin_11,player):
                    if state_plant_11 == 1:
                        money += 2
                    
                    if state_plant_11 == 2:
                        money += 6
                    
                    if state_plant_11 == 3:
                        money += 11
                        
                    coin_11.kill()
                    state_coin_11 = 0
                    state_plant_11 = 0
                    
            if coins.has(coin_12):
                if sprite.collide_rect(player,coin_12):
                    if state_plant_12 == 1:
                        money += 2
                    
                    if state_plant_12 == 2:
                        money += 6
                    
                    if state_plant_12 == 3:
                        money += 11
                        
                    coin_12.kill()
                    state_coin_12 = 0
                    state_plant_12 = 0

        display.update()
        clock.tick(FPS)
menu()
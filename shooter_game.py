from pygame import * 
 
window = display.set_mode((700,500)) 
background = transform.scale(image.load('city_2.png'),(700,500)) 
 
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (65, 65))     
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
bullets = sprite.Group() 
 
class Player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_LEFT] and self.rect.x > 5: 
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < 700 - 80: 
            self.rect.x += self.speed 
 
 
 

 
class Bullet(GameSprite): 
    def update(self): 
        self.rect.y -= self.speed 
        if self.rect.y < 0: 
            self.kill() 
 
score = 0 
lost = 0 
 
from random import * 
class Enemy(GameSprite): 
    def update(self): 
        self.rect.y += self.speed 
        global lost 
        if self.rect.y > 500: 
            self.rect.x = randint(50, 650) 
            self.rect.y = -50 
            lost += 1 
barigadas = sprite.Group()
monsters = sprite.Group()
class Asteroid(GameSprite): 
    def update(self): 
        self.rect.y += self.speed 
        if self.rect.y > 500: 
            self.rect.x = randint(50, 650) 
            self.rect.y = -50  

for i in range(3):
    barigada = Asteroid('Asset 7@4x.png',randint(500,700), randint(-250,0), 2)
    barigadas.add(barigada) 
 
for i in range(5): 
    monster = Enemy('bomb-4.png', randint(50,650), randint(-350,0), 5) 
    monsters.add(monster) 
 
Hero = Player('princess_1.png', 350, 450, 5) 
run = True 
 
clock = time.Clock() 
################################################## 
begaet_chel = True 
 

font.init() 
font1 = font.Font(None, 36) 

text_score = font1.render('тип крутой'  + str(score), 1, (255,255,255) ) 
text_lost = font1.render('лошпедус'  + str(score), 1, (255,255,255)) 
 
 
while run: 
 
    text_score = font1.render('Счет: ' + str(score), 1, (255,255,255)) 
    text_lost = font1.render('Пропустил: ' + str(lost), 1, (255,255,255)) 
 
    window.blit(background, (0,0)) 
    window.blit(text_score, (0,0)) 
    window.blit(text_lost, (0,50)) 
 
 
    monsters.draw(window) 
 
    barigadas.draw(window)
    bullets.draw(window) 
 
 
    if begaet_chel: 
        bullets.update() 
        Hero.update() 
        monsters.update() 
        barigadas.update()
    
    
    Hero.reset() 
 
    if lost >= 5: 
        window.blit(font1.render('лошпедус', 1, (255,255,255 )), (300, 200)) 
        begaet_chel = False  
         
 
     
 
     
    if sprite.spritecollide( Hero, monsters, False): 
        window.blit(font1.render('квутой', 1, (255,255,255 )), (300, 200)) 
        begaet_chel = False 
         
    if score >= 10: 
        window.blit(font1.render('хихихаха', 1, (255,255,255 )), (300, 200)) 
        begaet_chel = False 
    
 
    if sprite.groupcollide(Hero, barigadas, True, True): 
        break  
 
        score = score + 1 
 
    for e in event.get(): 
        if e.type == QUIT: 
            run = False 
        elif e.type == KEYDOWN: 
            if e.key == K_SPACE: 
                Hero.fire() 
         
     
    display.update() 
    clock.tick(60)








#5810404936 Yarnadhis Kapaeng 

import pygame , sys , time , random 

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()

white = (255,255,255)
black =(0,0,0)
darkgrey = (40,40,40)
red = (255,0,0)

displayW = 800
displayH = 600
blockSize = 30
monSize = 30
meleeSize = 15
ammoSize = 10
gunRange = 500
bgList = [pygame.image.load('background/bg1.png'),pygame.image.load('background/bg2.png'),pygame.image.load('background/bg3.png'),\
              pygame.image.load('background/bg4.png'),pygame.image.load('background/bg5.png'),pygame.image.load('background/bg6.png'),\
              pygame.image.load('background/bg7.png'),pygame.image.load('background/bg8.png')]
background1 = pygame.image.load('background/bg1.png')
FPS = 80

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((displayW,displayH))
pygame.display.set_caption('Angry Ducks 5810404936 Yarnadhis Kapaeng')
blankImg = pygame.image.load('blank.png')

background = pygame.Surface(gameDisplay.get_size())
background = background.convert()


front = pygame.image.load('menu/front.png')
playMenu = pygame.image.load('menu/redPlay.png')
quitMenu = pygame.image.load('menu/redQuit.png')
howtoMenu = pygame.image.load('menu/redHowto.png')
howtoScreen = pygame.image.load('menu/howto2.png')
stageClear = pygame.image.load('menu/stageClear.png')
gameOverImg = pygame.image.load('menu/gameover.png')
pauseMenu = pygame.image.load('menu/mainPause.png')
resumeMenu = pygame.image.load('menu/redResume.png')
restartMenu = pygame.image.load('menu/redRestart.png')
mainMenu = pygame.image.load('menu/redMain.png')
blackFade = pygame.image.load('menu/blackFade.png')
zzzImg = pygame.image.load('menu/zzz5.png')
bgImg = pygame.image.load('bg.png')
heroList = []
herolength = 1

headShotSound = pygame.mixer.Sound('sound2/Headshot.wav')
akSound = pygame.mixer.Sound('sound2/AK.wav')
blopSound = pygame.mixer.Sound('sound2/Blop.wav')
derpSound = pygame.mixer.Sound('sound2/Derp.wav')
kickSound = pygame.mixer.Sound('sound2/Kick.wav')
knifeSound = pygame.mixer.Sound('sound2/Knife.wav')
quackSound = pygame.mixer.Sound('sound2/quack.wav')
mQuackSound = pygame.mixer.Sound('sound2/macquack.wav')
snapSoumd = pygame.mixer.Sound('sound2/Snap.wav')
boopSound = pygame.mixer.Sound('sound2/Throw.wav')
aHitSound = pygame.mixer.Sound('sound2/appleHit3.wav')
fatalSound = pygame.mixer.Sound('sound2/fatality.wav')
clickSound = pygame.mixer.Sound('sound2/click2.wav')
marioSound = pygame.mixer.Sound('sound2/marioEnd.wav')
restartSound = pygame.mixer.Sound('sound2/restart2.wav')
class Ammo :
    def __init__(self,x,y,turn):
        self.x = x
        self.y = y
        self.xchange = 0
        self.ychange = 0
        self.turn = turn
        self.ammoSpeed = 4
        self.reloadInit = 20
        if self.turn == 'left':
            self.ammoImg = pygame.image.load('duck/atk/bullet_left.png')
        if self.turn == 'right':
            self.ammoImg = pygame.image.load('duck/atk/bullet_right.png')
        if self.turn == 'down':
            self.ammoImg = pygame.image.load('duck/atk/bullet_down.png')
        if self.turn == 'up':
            self.ammoImg = pygame.image.load('duck/atk/bullet_up.png')
        self.reload = self.reloadInit 
        
    def checkAmmoOverlap(self,other):
        if (((self.x+ammoSize > other.x) or (self.x > other.x)) \
            and ((self.x+ammoSize < other.x+monSize) or (self.x < other.x+monSize))) \
            and (((self.y+ammoSize > other.y) or (self.y > other.y)) \
            and ((self.y+ammoSize < other.y+monSize) or (self.y < other.y+monSize))) :
            return True
        else :
            return False
    def checkAmmoHitWall(self):
        if self.x+ammoSize >= displayW or self.x <= 0  or self.y+ammoSize >= displayH or self.y <=0 :
            return True 
        else :
            return False
                   
    def shoot(self):
            
        if self.turn == 'left' :
            self.xchange = -self.ammoSpeed
            self.ychange = 0
        if self.turn == 'right' :
            self.xchange = self.ammoSpeed
            self.ychange = 0
        if self.turn == 'down' :
            self.xchange = 0
            self.ychange = self.ammoSpeed
        if self.turn == 'up':
            self.xchange = 0
            self.ychange = -self.ammoSpeed
        self.x += self.xchange
        self.y += self.ychange

    def update(self):
        self.shoot()  
        if self.turn == 'left' :
            gameDisplay.blit(self.ammoImg ,[self.x,self.y+15])
        if self.turn == 'right' :
            gameDisplay.blit(self.ammoImg ,[self.x,self.y+15])
        if self.turn == 'up' :
            gameDisplay.blit(self.ammoImg ,[self.x+15,self.y])
        if self.turn == 'down' :
            gameDisplay.blit(self.ammoImg ,[self.x+15,self.y])


class Item:

    def __init__(self):
        self.x = round(random.randrange(blockSize,displayW-monSize-blockSize)/2)*2
        self.y = round(random.randrange(blockSize,displayH-monSize-blockSize)/2)*2
        #self.gunImg = [pygame.image.load('duck/item/gun1.png')]
        self.timeInitItem = 5
        self.timeItem = self.timeInitItem 
        self.itemFrame = 0
        self.itemFloat = [pygame.image.load('duck/item/gun1.png'),pygame.image.load('duck/item/gun2.png'),pygame.image.load('duck/item/gun3.png'),\
                          pygame.image.load('duck/item/gun4.png'),pygame.image.load('duck/item/gun5.png'),pygame.image.load('duck/item/gun6.png')]                       
        self.getPos()
    def getPos(self):
        while True :
            tempX = round(random.randrange(blockSize,displayW-monSize-blockSize)/2)*2
            tempY = round(random.randrange(blockSize,displayH-monSize-blockSize)/2)*2
            if (((player.x+blockSize+50 > tempX) or (player.x > tempX)) and ((player.x+blockSize+50 < tempX+monSize) or (self.x < tempX+monSize))) \
            and( ((player.y+blockSize+50 > tempY) or (player.y > tempY)) and ((player.y+blockSize+50 < tempY+monSize) or (player.y < tempY+monSize))) :
                continue
            else :
                break
        self.x = tempX
        self.y = tempY

    def animate(self) :
        if self.timeItem == 0 :
            if self.itemFrame == 5:
                self.itemFrame = 0
            else:
                self.itemFrame += 1
            self.timeItem = self.timeInitItem
        else :
            self.timeItem -=1
        gameDisplay.blit(self.itemFloat[self.itemFrame], [self.x, self.y])
        
    def update(self):
        self.animate()
        #gameDisplay.blit(self.gunImg, (self.x, self.y))       
class Hero :
    
    def __init__(self, x=displayW/2-blockSize, y=displayH/2-blockSize):
        self.x = x
        self.y = y
        self.xchange = 0
        self.ychange = 0
        self.walkFrame = 0
        self.meleeFrame = 0
        self.gunFrame = 0
        self.mode = 'melee'  # melee , range 
        #self.runFrame = False
        ##############################################
        self.meleeLeft = [pygame.image.load('duck/atk/atk_left1.png'), pygame.image.load('duck/atk/atk_left2.png'),pygame.image.load('duck/atk/atk_left3.png'),\
                                pygame.image.load('duck/atk/atk_left4.png'),pygame.image.load('duck/atk/atk_left5.png'),pygame.image.load('duck/atk/atk_left6.png'),\
                                pygame.image.load('duck/atk/atk_left7.png')]
        self.meleeRight = [pygame.image.load('duck/atk/atk_right1.png'), pygame.image.load('duck/atk/atk_right2.png'),pygame.image.load('duck/atk/atk_right3.png'),\
                                pygame.image.load('duck/atk/atk_right4.png'),pygame.image.load('duck/atk/atk_right5.png'),pygame.image.load('duck/atk/atk_right6.png'),\
                                pygame.image.load('duck/atk/atk_right7.png')]
        self.meleeUp = [pygame.image.load('duck/atk/atk_up1.png'), pygame.image.load('duck/atk/atk_up2.png'),pygame.image.load('duck/atk/atk_up3.png'),\
                                pygame.image.load('duck/atk/atk_up4.png'),pygame.image.load('duck/atk/atk_up5.png'),pygame.image.load('duck/atk/atk_up6.png'),\
                                pygame.image.load('duck/atk/atk_up7.png')]
        self.meleeDown = [pygame.image.load('duck/atk/atk_down1.png'), pygame.image.load('duck/atk/atk_down2.png'),pygame.image.load('duck/atk/atk_down3.png'),\
                                pygame.image.load('duck/atk/atk_down4.png'),pygame.image.load('duck/atk/atk_down5.png'),pygame.image.load('duck/atk/atk_down6.png'),\
                                pygame.image.load('duck/atk/atk_down7.png')]
        self.meleeAttackAll = [self.meleeUp,self.meleeDown,self.meleeLeft,self.meleeRight]
        self.meleeAttack = [blankImg,blankImg,blankImg,blankImg,blankImg,blankImg,blankImg] #7
        ##############################################
        self.duckUp = [pygame.image.load('duck/duck_up1.png'),pygame.image.load('duck/duck_up2.png'),\
                       pygame.image.load('duck/duck_up3.png'),pygame.image.load('duck/duck_up4.png'),]
        self.duckDown = [pygame.image.load('duck/duck_down1.png'),pygame.image.load('duck/duck_down2.png'),\
                         pygame.image.load('duck/duck_down3.png'),pygame.image.load('duck/duck_down4.png'),]
        self.duckLeft = [pygame.image.load('duck/duck_left1.png'),pygame.image.load('duck/duck_left2.png'),\
                         pygame.image.load('duck/duck_left3.png'),pygame.image.load('duck/duck_left4.png'),]
        self.duckRight = [pygame.image.load('duck/duck_right1.png'),pygame.image.load('duck/duck_right2.png'),\
                          pygame.image.load('duck/duck_right3.png'),pygame.image.load('duck/duck_right4.png'),]
        self.duckWalkAll = [self.duckUp,self.duckDown,self.duckLeft,self.duckRight]
        self.duckWalk = [blankImg,blankImg,blankImg,blankImg] #4  
        ##############################################
        self.gunUp = [pygame.image.load('duck/atk/gun_up1.png'),pygame.image.load('duck/atk/gun_up2.png'),\
                       pygame.image.load('duck/atk/gun_up3.png'),pygame.image.load('duck/atk/gun_up4.png'),]
        self.gunDown = [pygame.image.load('duck/atk/gun_down1.png'),pygame.image.load('duck/atk/gun_down2.png'),\
                         pygame.image.load('duck/atk/gun_down3.png'),pygame.image.load('duck/atk/gun_down4.png'),]
        self.gunLeft = [pygame.image.load('duck/atk/gun_left1.png'),pygame.image.load('duck/atk/gun_left2.png'),\
                         pygame.image.load('duck/atk/gun_left3.png'),pygame.image.load('duck/atk/gun_left4.png'),]
        self.gunRight = [pygame.image.load('duck/atk/gun_right1.png'),pygame.image.load('duck/atk/gun_right2.png'),\
                          pygame.image.load('duck/atk/gun_right3.png'),pygame.image.load('duck/atk/gun_right4.png'),]
        self.gunAttackAll = [self.gunUp,self.gunDown,self.gunLeft,self.gunRight]
        self.gunAttack = [blankImg,blankImg,blankImg,blankImg] #4  
        ##############################################
        self.glassesUp = pygame.image.load('duck/glasses_up.png')
        self.glassesDown = pygame.image.load('duck/glasses_down.png')
        self.glassesLeft = pygame.image.load('duck/glasses_left.png')
        self.glassesRight = pygame.image.load('duck/glasses_right.png')
        ##############################################        
        #self.turn = 'down'  #default is down
        self.turns = ['down']
        self.img = blankImg
        self.timeInitMelee = 2
        self.timeMelee = self.timeInitMelee
        self.timeInitWalk = 5
        self.timeWalk = self.timeInitWalk
        self.timeInitGun = 10
        self.timeGun = self.timeInitGun
        self.attack = False

        self.death = False

    @property
    def turn(self):
        return self.turns[0]

    @turn.setter
    def turn(self, value):
        self.turns = [value]
        

       
    def resetPos(self):
        self.turn = 'down' 
        self.img = blankImg
        self.x = displayW/2-blockSize
        self.y = displayH/2-blockSize
        self.xchange = 0
        self.ychange = 0
        self.walkFrame = 0
        self.meleeFrame = 0
        self.gunFrame = 0
        
    def checkHeroOverlab(self,other):
        if ((self.x+blockSize > other.x) or (self.x > other.x)) \
        and ((self.x+blockSize < other.x+monSize) or (self.x < other.x+monSize)) :
            if ((self.y+blockSize > other.y) or (self.y > other.y)) \
            and ((self.y+blockSize < other.y+monSize) or (self.y < other.y+monSize)) :
                return True
        else :
            return False
    def animateGun(self) :
        if self.timeGun == 0 :
            if self.gunFrame == 3:
                self.gunFrame = 0

            else:
                self.gunFrame += 1
            self.timeGun = self.timeInitGun
        else :
            self.timeGun -=1
        if self.turn == 'left' :
            gameDisplay.blit(self.gunAttack[self.gunFrame], [self.x-20, self.y])
        if self.turn == 'up' :
            gameDisplay.blit(self.gunAttack[self.gunFrame], [self.x, self.y-20])
        if self.turn == 'down' or self.turn == 'right' :
            gameDisplay.blit(self.gunAttack[self.gunFrame], [self.x, self.y])

            
        
        
    def checkInRangeGun(self,other) :
        if self.turn == 'left' and (self.x > other.x):
            if ((self.x+blockSize-other.x+monSize <= gunRange) or (self.x - other.x <= gunRange)) \
                and (((self.y+blockSize > other.y-40) or (self.y > other.y-40)) \
                and ((self.y+blockSize < other.y+monSize+40) or (self.y < other.y+monSize+40))) :
                return True
        if self.turn == 'right' and (other.x > self.x ):
            if ((other.x+monSize-self.x+blockSize  <= gunRange) or (other.x - self.x <= gunRange)) \
                and (((self.y+blockSize > other.y-40) or (self.y > other.y-40)) \
                and ((self.y+blockSize < other.y+monSize+40) or (self.y < other.y+monSize+40))) :
                return True 
        if self.turn == 'down' and (other.y > self.y) :
            if ((other.y+monSize-self.y+blockSize  <= gunRange) or (other.y - self.y <= gunRange)) \
                and (((self.x+blockSize > other.x-40) or (self.x > other.x-40)) \
                and ((self.x+blockSize < other.x+monSize+40) or (self.x < other.x+monSize+40))) :
                return True 
        if self.turn == 'up' and (self.y > other.y):
            if ((self.y+blockSize-other.y+monSize  <= gunRange) or (self.y - other.y <= gunRange)) \
                and (((self.x+blockSize > other.x-40) or (self.x > other.x-40)) \
                and ((self.x+blockSize < other.x+monSize+40) or (self.x < other.x+monSize+40))) :
                return True 
            
    def checkInRangeMelee(self,other) :
        #print('                                                                                            ') #check
        if self.turn == 'left' :
            if (((self.x-meleeSize > other.x) or (self.x > other.x)) \
            and ((self.x-meleeSize < other.x+monSize) or (self.x < other.x+monSize))) and\
                 (((self.y+blockSize > other.y-meleeSize) or (self.y > other.y-meleeSize)) \
                and ((self.y+blockSize < other.y+monSize+meleeSize) or (self.y < other.y+monSize+meleeSize))) :
                    return True
                
            else :
                return False
            
        if self.turn == 'right' :
            if (((self.x+blockSize+meleeSize > other.x) or (self.x+blockSize > other.x)) \
            and ((self.x+blockSize+meleeSize < other.x+monSize) or (self.x+blockSize < other.x+monSize))) and\
                (((self.y+blockSize > other.y-meleeSize) or (self.y > other.y-meleeSize)) \
                and ((self.y+blockSize < other.y+monSize+meleeSize) or (self.y < other.y+monSize+meleeSize))) :
                    return True
            else :
                return False
        if self.turn == 'up' :
            if (((self.y-meleeSize > other.y) or (self.y > other.y)) \
            and ((self.y-meleeSize < other.y+monSize) or (self.y < other.y+monSize))) and\
                (((self.x+blockSize > other.x-meleeSize) or (self.x > other.x-meleeSize)) \
                   and ((self.x+blockSize < other.x+monSize+meleeSize) or (self.x < other.x+monSize+meleeSize))) :
                    return True
            else :
                return False
        if self.turn == 'down' :
            if (((self.y+blockSize+meleeSize > other.y) or (self.y+blockSize > other.y)) \
            and ((self.y+blockSize+meleeSize < other.y+monSize) or (self.y+blockSize < other.y+monSize))) and\
                (((self.x+blockSize > other.x-meleeSize) or (self.x > other.x-meleeSize)) \
                   and ((self.x+blockSize < other.x+monSize+meleeSize) or (self.x < other.x+monSize+meleeSize))) :
                    return True
            else :
                return False
        
  
    def meleeX(self):
        x = self.x
        if self.turn == 'left' :
            x -= 25
            y -= 25
        if self.turn =='right' :
            x += meleeSize
        return x
    def meleeY(self):
        y = self.y
        if self.turn == 'up' :
            y -= meleeSize
        if self.turn == 'down' :
            y += meleeSize
        return y
    
   
    def doMeleeAttack(self):
      #  print (self.meleeFrame,self.attack)
##        print(self.attack, self.timeMelee != self.timeInitMelee, self.meleeFrame != 0)
##        print(self.timeMelee,self.meleeFrame )
        if self.attack or self.timeMelee != self.timeInitMelee or self.meleeFrame != 0:
            self.attack = False
            if self.timeMelee == 0 :
                if self.meleeFrame == 6:
                    self.meleeFrame = 0
                    #self.attack = False 
                else:
                    self.meleeFrame += 1
                self.timeMelee = self.timeInitMelee
            else :
                self.timeMelee -=1
            gameDisplay.blit(self.meleeAttack[self.meleeFrame], [self.x-25, self.y-25])
        
    def dead(self):
        self.death = True
        self.img = pygame.image.load('duck/skull.png')
        #gameDisplay.blit(self.img ,[self.x,self.y])
        
    def animateWalk(self):       
        if self.timeWalk == 0 :
            if self.walkFrame == 3 :
                self.walkFrame = 0
            else:
                self.walkFrame += 1
            self.timeWalk = self.timeInitWalk
        else :
            self.timeWalk -=1  
        gameDisplay.blit(self.duckWalk[self.walkFrame], [self.x, self.y])
        
    def walk(self):
        if self.turn == 'right':
            self.xchange = 2
            self.ychange = 0
        elif self.turn == 'left':
            self.xchange = -2
            self.ychange = 0
        elif self.turn == 'down':
            self.xchange = 0
            self.ychange = 2
        elif self.turn == 'up':
            self.xchange = 0
            self.ychange = -2
        self.x += self.xchange
        self.y += self.ychange
        direction = {'right':3,'left':2,'down':1,'up':0} #temp
        self.duckWalk = self.duckWalkAll[direction[self.turn]]
        self.meleeAttack = self.meleeAttackAll[direction[self.turn]]
        self.gunAttack = self.gunAttackAll[direction[self.turn]] 
    def update(self):
        self.walk()
        self.animateWalk()
        #gameDisplay.blit(self.img, (self.x, self.y))
  
            
        
        
class monster :
    opposite_turn = {'right' : 'left', 'left' : 'right', 'up' : 'down', 'down' : 'up'}
    def __init__(self):
        self.respawn()
##        self.x = round(random.randrange(blockSize,displayW-monSize-blockSize)/2)*2
##        self.y = round(random.randrange(blockSize,displayH-monSize-blockSize)/2)*2
        self.xchange = 0
        self.ychange = 0     
        self.turn = random.choice(['right', 'left', 'up', 'down'])
        self.range = self.randRange()
        self.img = blankImg
        self.frame = 0
        self.monsterWalk = [blankImg,blankImg]
        self.timeInit = 10
        self.time = self.timeInit
        ##############################################
        self.blueDown = [pygame.image.load('PacGhost/blue/blue_down1.png'), pygame.image.load('PacGhost/blue/blue_down2.png')]
        self.blueUp =[pygame.image.load('PacGhost/blue/blue_up1.png'), pygame.image.load('PacGhost/blue/blue_up2.png')]
        self.blueLeft =[pygame.image.load('PacGhost/blue/blue_left1.png'), pygame.image.load('PacGhost/blue/blue_left2.png')]
        self.blueRight =[pygame.image.load('PacGhost/blue/blue_right1.png'), pygame.image.load('PacGhost/blue/blue_right2.png')]
        ##############################################
        self.redDown = [pygame.image.load('PacGhost/red/red_down1.png'), pygame.image.load('PacGhost/red/red_down2.png')]
        self.redUp =[pygame.image.load('PacGhost/red/red_up1.png'), pygame.image.load('PacGhost/red/red_up2.png')]
        self.redLeft =[pygame.image.load('PacGhost/red/red_left1.png'), pygame.image.load('PacGhost/red/red_left2.png')]
        self.redRight =[pygame.image.load('PacGhost/red/red_right1.png'), pygame.image.load('PacGhost/red/red_right2.png')]
        ##############################################
        self.pinkDown = [pygame.image.load('PacGhost/pink/pink_down1.png'), pygame.image.load('PacGhost/pink/pink_down2.png')]
        self.pinkUp =[pygame.image.load('PacGhost/pink/pink_up1.png'), pygame.image.load('PacGhost/pink/pink_up2.png')]
        self.pinkLeft =[pygame.image.load('PacGhost/pink/pink_left1.png'), pygame.image.load('PacGhost/pink/pink_left2.png')]
        self.pinkRight =[pygame.image.load('PacGhost/pink/pink_right1.png'), pygame.image.load('PacGhost/pink/pink_right2.png')]
        ##############################################
        self.orangeDown = [pygame.image.load('PacGhost/orange/orange_down1.png'), pygame.image.load('PacGhost/orange/orange_down2.png')]
        self.orangeUp =[pygame.image.load('PacGhost/orange/orange_up1.png'), pygame.image.load('PacGhost/orange/orange_up2.png')]
        self.orangeLeft =[pygame.image.load('PacGhost/orange/orange_left1.png'), pygame.image.load('PacGhost/orange/orange_left2.png')]
        self.orangeRight =[pygame.image.load('PacGhost/orange/orange_right1.png'), pygame.image.load('PacGhost/orange/orange_right2.png')]
        ##############################################
        self.colorPick = random.randrange(1,5) #1blue 2red 3pink 4orange , colorPick is just for random
        if self.colorPick == 1 :
            self.monsterWalkAll = [self.blueUp,self.blueDown,self.blueLeft,self.blueRight]
        if self.colorPick == 2 :
            self.monsterWalkAll = [self.redUp,self.redDown,self.redLeft,self.redRight]
        if self.colorPick == 3 :
            self.monsterWalkAll = [self.pinkUp,self.pinkDown,self.pinkLeft,self.pinkRight]
        if self.colorPick == 4 :
            self.monsterWalkAll = [self.orangeUp,self.orangeDown,self.orangeLeft,self.orangeRight]
        ##############################################
        self.spawnImg = [pygame.image.load('PacGhost/spawn/spawn1.png'),pygame.image.load('PacGhost/spawn/spawn2.png'),\
                         pygame.image.load('PacGhost/spawn/spawn3.png'),pygame.image.load('PacGhost/spawn/spawn4.png'),\
                         pygame.image.load('PacGhost/spawn/spawn5.png'),pygame.image.load('PacGhost/spawn/spawn6.png'),\
                         pygame.image.load('PacGhost/spawn/spawn7.png'),pygame.image.load('PacGhost/spawn/spawn8.png'),\
                         pygame.image.load('PacGhost/spawn/spawn9.png'),pygame.image.load('PacGhost/spawn/spawn10.png'),\
                         pygame.image.load('PacGhost/spawn/spawn11.png'),pygame.image.load('PacGhost/spawn/spawn11.png'),\
                         pygame.image.load('PacGhost/spawn/spawn11.png'),pygame.image.load('PacGhost/spawn/spawn12.png'),\
                         pygame.image.load('PacGhost/spawn/spawn12.png'),pygame.image.load('PacGhost/spawn/spawn11.png'),\
                         pygame.image.load('PacGhost/spawn/spawn11.png'),pygame.image.load('PacGhost/spawn/spawn12.png'),\
                         pygame.image.load('PacGhost/spawn/spawn12.png'),pygame.image.load('PacGhost/spawn/spawn11.png'),\
                         pygame.image.load('PacGhost/spawn/spawn11.png')] #21frame
        self.death = False

    def dead(self):
        self.death = True
        self.img = pygame.image.load('PacGhost/deadGhost.png')

    def respawn(self):

        while True :
            tempX = round(random.randrange(blockSize,displayW-monSize-blockSize)/2)*2
            tempY = round(random.randrange(blockSize,displayH-monSize-blockSize)/2)*2
            if (((player.x+blockSize+50 > tempX) or (player.x > tempX)) and ((player.x+blockSize+50 < tempX+monSize) or (player.x < tempX+monSize))) \
            and( ((player.y+blockSize+50 > tempY) or (player.y > tempY)) and ((player.y+blockSize+50 < tempY+monSize) or (player.y < tempY+monSize))) :
                continue
            else :
                break

        self.x = tempX
        self.y = tempY
                    
        
    def randTurn(self):
        turns = ['right', 'left', 'up', 'down']
        turns.remove(self.opposite_turn[self.turn])
        return random.choice(turns)
    def randRange(self):
        return random.randrange(10,40)
    def walk(self):
        if self.turn == 'right':
            self.xchange = 2
            self.ychange = 0
        elif self.turn == 'left':
            self.xchange = -2
            self.ychange = 0
        elif self.turn == 'down':
            self.xchange = 0
            self.ychange = 2
        elif self.turn == 'up':
            self.xchange = 0
            self.ychange = -2
        if self.x + self.xchange + blockSize >= displayW or self.x + self.xchange <= 0 \
           or self.y + self.ychange +blockSize >= displayH or self.y + self.ychange <=0 :
            self.turn = self.randTurn()
            self.range = self.randRange()
            self.walk()
        else:
            self.x += self.xchange
            self.y += self.ychange
        direction = {'right':3,'left':2,'down':1,'up':0} #temp
        self.monsterWalk = self.monsterWalkAll[direction[self.turn]]
        
    def animateWalk(self):       
        if self.time == 0 :
            if self.frame == 1 :
                self.frame = 0
            else:
                self.frame += 1
            self.time = self.timeInit
        else :
            self.time -=1
        
        gameDisplay.blit(self.monsterWalk[self.frame], [self.x, self.y])
    def update(self):
        if self.range == 0:
            self.turn = self.randTurn()
            self.range = self.randRange()
        else:
            self.range -= 1
        self.walk()
        self.animateWalk()
        #gameDisplay.blit(self.img, (self.x, self.y))
        

        
def drawGrid():
    for x in range(0, displayW, blockSize): # draw vertical lines
        pygame.draw.line(gameDisplay, darkgrey, (x, 0), (x, displayH))
    for y in range(0, displayH, blockSize): # draw horizontal lines
        pygame.draw.line(gameDisplay, darkgrey, (0, y), (displayW, y))
        
def message_to_screen(msg,size,color,posX,posY):
    font = pygame.font.SysFont('Edo',size)
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text ,[posX, posY])

 
def menuScreen() :
    pygame.mixer.music.stop()
    pygame.mixer.music.load('sound/Battlefield.mp3')
    pygame.mixer.music.play(-1)
    howto = False 
    menuBar = 1
    gameExit = False 
    while gameExit == False :
        #gameDisplay.fill(white)
        gameDisplay.blit(front,[0,0])

##        message_to_screen('DUCK & FRIEND',80,black,175,150)
##        message_to_screen('PLAY',40,black,355,270)
##        message_to_screen('HOW TO PLAY',40,black,280,350)
        if menuBar == 1 :     
            gameDisplay.blit(playMenu ,[0, 0])
        if menuBar == 2 :
            gameDisplay.blit(howtoMenu ,[0, 0])            
        if menuBar == 3 :
            gameDisplay.blit(quitMenu ,[0, 0])
        if howto == True :
            gameDisplay.blit(howtoScreen,[0,0])
       
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT :
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if howto == False :
                        gameExit = True
                    elif howto == True :
                        howto = False 
                if event.key == pygame.QUIT :
                    gameExit = True

                if event.key == pygame.K_LEFT:
                    if menuBar != 1 :
                        pygame.mixer.Sound.play(clickSound)                    
                    if menuBar == 3 :
                        menuBar = 2
                    elif menuBar == 2 :
                        menuBar = 1
                  #  print(menuBar)
                        
                if event.key == pygame.K_RIGHT:
                    if menuBar != 3:
                        pygame.mixer.Sound.play(clickSound)
                    if menuBar == 1 :
                        menuBar = 2
                    elif menuBar == 2 :
                        menuBar = 3
                   # print(menuBar) 
                if event.key == pygame.K_RETURN :
                    if menuBar == 1 :
                        player.resetPos()
                        
                        items = []
                        dead_heros = []
                        dead_monsters =[]
                        ammoList = []
                        monsterList = [monster()]

                        zzz = True
                        
                        gameLoop()
                    if menuBar == 3 :
                        pygame.quit()
                        quit()
                    if menuBar == 2 :
                        howto = True 
                        
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

def gameLoop():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('sound/Chillstep2.mp3')
    pygame.mixer.music.play(-1)
    
    global heros, player
    respawnItem = 700
    gameExit = gameOver = endStage = False
    level = 1
    deadStat = False
    attacking = False
    items = []
    monsterList = [monster()]
    ammoList = []
    ammoReloadInit = 100
    ammoReload = ammoReloadInit
    turn = 'down'
    dead_heros = []
    dead_monsters = []
    monsters_num = level * 5 - 1
    spawn_time = 700
    pause = False
    pauseBar = 1
    zzz = True
    score = 0
    bgPermission = True
    heros = [player]
     
    while gameExit == False :

        while pause :
            pygame.mixer.music.pause()
            gameDisplay.blit(pauseMenu,[0,0])
            if pauseBar == 1 :
                gameDisplay.blit(resumeMenu,[0,0])
            if pauseBar == 2 :
                gameDisplay.blit(restartMenu,[0,0])
            if pauseBar == 3 :
                gameDisplay.blit(mainMenu,[0,0])
            pygame.display.update()            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.unpause()
                        pause = False                      
                    if event.key == pygame.K_DOWN :
                        pygame.mixer.Sound.play(clickSound)
                        if pauseBar == 1:
                            pauseBar = 2
                        elif pauseBar == 2:
                            pauseBar = 3
                    if event.key == pygame.K_UP :
                        pygame.mixer.Sound.play(clickSound)
                        if pauseBar == 3 :
                            pauseBar = 2
                        elif pauseBar == 2 :
                            pauseBar = 1
                    if event.key == pygame.K_RETURN :
                        if pauseBar == 1 :
                            pygame.mixer.music.unpause()
                            pause = False
                        if pauseBar == 2 :
                            score = 0
                            player.resetPos()
                            heros = [player]                
                            gameOver = False
                            gameLoop()
                        if pauseBar == 3 :

                            menuScreen()
##                    if event.key == pygame.K_b :
##                        if bgPermission == True :
##                            bgPermission = False
##                        elif bgPermission == False :
##                            bgPermission = True
                if event.type == pygame.QUIT :
                    pause = False 
                    gameExit = True
                    
        while gameOver == True :
            #message_to_screen('Game Over',100,white,120,200)            
            #pygame.mixer.music.stop()
                
            gameDisplay.blit(gameOverImg,[0,0,])
            message_to_screen('Press Space to play again',50,white,100,350)
            pygame.display.update()
    
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_SPACE :                 
                        pygame.mixer.music.stop()
                        player.resetPos()
                        heros = [player]
                        marioPlay = False 
                        gameOver = False
                        gameLoop()                
                if event.type == pygame.QUIT :
                    gameExit = True
                    gameOver = False
        if bgPermission :        
            background.blit(bgList[level%7],[0,0])
        gameDisplay.blit(background, (0, 0))
        message_to_screen(('%d points' %score), 24,white,670,25)    
        #gameDisplay.fill(white)
        #drawGrid()       
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                gameExit = True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    pause = True 
                    
                if event.key == pygame.K_LEFT and player.turn != 'right':
                    turn = 'left'
            
                if event.key == pygame.K_RIGHT and player.turn != 'left' :
                    turn = 'right'


                if event.key == pygame.K_DOWN and player.turn != 'up':
                    turn = 'down'
     

                if event.key == pygame.K_UP and player.turn != 'down':
                    turn = 'up'
                #if event.key == pygame.K_SPACE:
                #    monsterList.append(monster())
        player = heros[0]        
        
        if player.x+blockSize >= displayW or player.x <= 0  or player.y+blockSize >= displayH or player.y <=0 :
            #pygame.mixer.Sound.play(derpSound)
            player.dead()
            gameOver = True
        player.turns.append(turn)
        for pos in range(1,len(heros)):  
            heros[pos].turns.append(heros[pos-1].turns[0])
        for pos in range(len(heros)):
            heros[pos].turns = heros[pos].turns[1:]
        player.update()
        for hero in heros[1:]:
            hero.update()
        for bullet in ammoList :
            bullet.update()
        if spawn_time == 0 and monsters_num > 0:
            spawn_time = 700
            monsterList.append(monster())
            monsters_num -= 1
        else:
            spawn_time -= 1
        for enemy in monsterList :
            for bullet in ammoList :
                if bullet.checkAmmoOverlap(enemy):
                    #enemy.respawn()
                    if len(monsterList) == 1 :
                        pygame.mixer.Sound.play(headShotSound)
                    else :
                        pygame.mixer.Sound.play(blopSound)
                    enemy.dead()
                    score += 1
                    dead_monsters.append([enemy, 50])
                    monsterList.remove(enemy)
                    if monsters_num > 0:
                        monsterList.append(monster())
                        monsters_num -= 1
                    ammoList.remove(bullet)
                if bullet.checkAmmoHitWall() :
                    ammoList.remove(bullet)

            if enemy in monsterList:

                if player.checkHeroOverlab(enemy):
                    #pygame.mixer.Sound.play(derpSound)
                    
                    player.dead()
                    gameOver = True 
               
                if player.checkInRangeMelee(enemy):
                    player.attack = True
                    #enemy.respawn()
                    pygame.mixer.Sound.play(knifeSound)
                    enemy.dead()
                    pygame.mixer.Sound.play(blopSound)
                    score += 1
                    dead_monsters.append([enemy, 50])
                    monsterList.remove(enemy)

                    if monsters_num > 0:
                        monsterList.append(monster())
                        monsters_num -= 1
                player.doMeleeAttack()

            for hero in heros[1:]:
                if hero in heros:
                    if hero.turn == 'left' :
                        gameDisplay.blit(hero.glassesLeft ,[hero.x,hero.y])
                    if hero.turn == 'right' :
                        gameDisplay.blit(hero.glassesRight ,[hero.x,hero.y])
                    if hero.turn == 'up' :
                        gameDisplay.blit(hero.glassesUp ,[hero.x,hero.y])
                    if hero.turn == 'down' :
                        gameDisplay.blit(hero.glassesDown ,[hero.x,hero.y])                    
                    if hero.checkHeroOverlab(enemy):
                        pygame.mixer.Sound.play(derpSound)
                        #heros = heros[:heros.index(hero)]
                        hero.dead()
                    if hero.checkInRangeGun(enemy) :
                        hero.animateGun()
                        if ammoReload == 0 :
                            pygame.mixer.Sound.play(akSound)
                            ammoList.append(Ammo(hero.x,hero.y,hero.turn))
                            ammoReload = ammoReloadInit
                        else :
                            ammoReload -= 1
            enemy.update()
            #player.turns.append(player.turn) #comment this
            
        respawnItem -= 1
        if respawnItem <= 0:
            items.append(Item())
            respawnItem = 700
        
        for item in items:
            item.update()
            
            if player.checkHeroOverlab(item):
                pygame.mixer.Sound.play(mQuackSound)
                items.remove(item)
                if heros[-1].turn == 'right':
                    heros.append(Hero(heros[-1].x - 30, heros[-1].y))
                    heros[-1].turns = ['right']*15
                elif heros[-1].turn == 'left':
                    heros.append(Hero(heros[-1].x + 30, heros[-1].y))
                    heros[-1].turns = ['left']*15
                elif heros[-1].turn == 'down':
                    heros.append(Hero(heros[-1].x, heros[-1].y - 30))
                    heros[-1].turns = ['down']*15
                elif heros[-1].turn == 'up':
                    heros.append(Hero(heros[-1].x, heros[-1].y + 30))
                    heros[-1].turns = ['up']*15
                                                
            #time.sleep(0.5)
        for hero in heros[1:]:
            if hero.death:
                dead_heros.append([hero, 50])
                heros = heros[:heros.index(hero)]
                break
            if hero not in heros:
                hero.dead()
                dead_heros.append([hero, 50])
        if heros[0].death:
            gameDisplay.blit(heros[0].img, (heros[0].x, heros[0].y))
        for died in dead_heros:
            gameDisplay.blit(died[0].img, (died[0].x, died[0].y))
            if died[1] == 0:
                dead_heros.remove(died)
            else:
                died[1] -= 1
        for died in dead_monsters:
            gameDisplay.blit(died[0].img, (died[0].x, died[0].y))
            if died[1] == 0:
                dead_monsters.remove(died)
            else:
                died[1] -= 1

        if monsters_num == 0 and monsterList == []:
            level += 1
            endStage = True
        if pause or zzz or gameOver :
            gameDisplay.blit(blackFade,[0,0])
        clock.tick(FPS)
       # player.update()
        pygame.display.update()
        while zzz :
            #pygame.mixer.music.pause()
            gameDisplay.blit(zzzImg,[0,0])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        pygame.mixer.music.unpause()
                        bgPermission = False 
                        zzz = False
##                    if event.key == pygame.K_UP:
##                        zzz = False
##                    if event.key == pygame.K_LEFT:
##                        zzz = False 
##                    if event.key == pygame.K_RIGHT:
##                        zzz = False
                if event.type == pygame.QUIT :
                    zzz = False  
                    gameExit = True
        while endStage:
            
           # message_to_screen('Stage Clear',100,white,120,200)
            gameDisplay.blit(stageClear,[0,0])
            message_to_screen(('Press Space to play level %s' %level),50,white,90,350)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False
                        endStage = False 
                    if event.key == pygame.K_SPACE : 
                        player.resetPos()
                        heros = [player]
                        items = []
                        dead_heros = []
                        dead_monsters =[]
                        spawn_time = 700
                        respawnItem = 700
                        ammoList = []
                        ammoReloadInit = 100
                        ammoReload = ammoReloadInit
                        monsterList = [monster()]
                        turn = 'down'
                        monsters_num = level * 5 - 1
                        zzz = True
                        bgPermission = True
                        
                        endStage = False              
                if event.type == pygame.QUIT :
                    endStage = False 
                    gameExit = True
        if gameOver :
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sound2/restart2.mp3')
            pygame.mixer.music.play(1)
    pygame.mixer.quit()
    pygame.quit()
    quit()
             
player = Hero()
heros = [player]
menuScreen()

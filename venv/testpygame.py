import pygame
import random
import math
#初始化界面
pygame.init()
screen = pygame.display.set_mode((800,600))#屏幕大小
pygame.display.set_caption('战斗机vs怪兽')#标题
icon = pygame.image.load('ufo.png')#获取图标
pygame.display.set_icon(icon)#载入图标
bgImg = pygame.image.load('bg.png')#获取背景图
#添加音效
pygame.mixer.music.load('bg.wav')
pygame.mixer.music.play(-1)#单曲循环
#添加射中音效
bong_sound = pygame.mixer.Sound('exp.wav')
#飞机
playerImg = pygame.image.load('player.png')#获取玩家飞机图
playerX = 400  #飞机横坐标
playerY = 500  #飞机纵坐标
playerStep = 0  #飞机移动速度
#分数
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
def show_score():
    text = f"Score:{score}"
    score_render = font.render(text, True, (0, 255, 0))
    screen.blit(score_render, (10, 10))
#游戏结束
is_over = False
over_font = pygame.font.Font('freesansbold.ttf',64)
def check_is_over():
    if is_over:
        text = "Game Over"
        score_render = over_font.render(text, True, (255, 0, 0))
        screen.blit(score_render, (250, 200))
#敌机
number_of_enemies = 6#敌机数
#怪兽类
class Enemy():
    def __init__(self):
        self.img = pygame.image.load('enemy.png')#获取怪兽图
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 200)
        self.step = random.randint(1, 4)#敌机移动速度
	#当被射中时，恢复位置
    def reset(self):
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 150)
enemies = []#保存所有的敌机
for i in range(number_of_enemies):
    enemies.append(Enemy())
#子弹类
class Bullet():
    def __init__(self):
        self.img = pygame.image.load('bullet.png')#获取子弹图
        self.x = playerX + 16
        self.y = playerY + 10
        self.step = 4 #子弹移动速度
	#击中
    def hit(self):
        global score
        for e in enemies:
            if(distance(self.x, self.y ,e.x, e.y) < 30):
                #射中
                bong_sound.play()
                bullets.remove(self)
                e.reset()
                score += 1
bullets = [] #保存现有的子弹
#显示敌机，并实现移动和下沉
def show_enemy():
    global is_over
    for e in enemies:
        screen.blit(e.img,(e.x, e.y))
        e.x += e.step
        #防止敌机出界
        if(e.x > 736 or e.x < 0):
            e.step *= -1
            e.y += 30  #敌机下沉
            if e.y > 450:
                is_over = True
                enemies.clear()
#显示玩家飞机
def move_player():
    global playerX
    playerX += playerStep #移动飞机
    #防止飞机出界
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0
#显示并移动子弹
def show_bullets():
    for b in bullets:
        screen.blit(b.img,(b.x, b.y))
        b.hit()#调用击中
        b.y -= b.step #移动子弹
        #子弹触界消失
        if b.y < 0:
            bullets.remove(b)
#检测两个点之间的距离
def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a ** 2 + b ** 2)
#游戏主循环
while True:
    screen.blit(bgImg,(0,0))#显示背景图
    show_score()#显示分数
    for event in pygame.event.get():#事件
        #退出
        if event.type == pygame.QUIT:
            pygame.quit()
           #通过键盘事件控制飞机的移动
        if event.type == pygame.KEYDOWN:#按下就移动
            if event.key == pygame.K_RIGHT:
                playerStep = 5
            elif event.key == pygame.K_LEFT:
                playerStep = -5
            elif event.key == pygame.K_SPACE:
                #创建一颗子弹
                bullets.append(Bullet())
       if event.type == pygame.KEYUP:#松开就停下
                playerStep = 0
       screen.blit(playerImg,(playerX, playerY))#显示玩家飞机
    move_player()#移动玩家
    show_enemy()#显示敌机
    show_bullets()#显示子弹
    check_is_over()#显示游戏结束
    pygame.display.update()  #更新界面
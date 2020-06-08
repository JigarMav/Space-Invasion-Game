import pygame
import random
import math

# initalise the pygame .
pygame.init()

# create a screen for our game.
screen = pygame.display.set_mode((800, 600))

# set title on the screen .
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship_icon.png")
pygame.display.set_icon(icon)

# background image
background = pygame.image.load("background.png")

# player
playerImg = pygame.image.load("player.png")
playerX = 380
playerY = 500
playerX_change = 0


def player(x, y):
    # blit means to draw. So we are drawing our player image on our screen.
    screen.blit(playerImg, (x, y))


# Enemy
no_of_enemies = 6
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
# form 6 enemies on the screen .
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(20, 100))
    enemyX_change.append(2)
    enemyY_change.append(40)



def enemy(x, y,i):
    # blit means to draw. So we are drawing our player image on our screen.
    screen.blit(enemyImg[i], (x, y))


# Bullet
# ready state shows its not on screen. and fired means on the screen.
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 8
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def collision(enemyX,enemyY, bulletX, bulletY):
    dist = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    if(dist<27):
        return True
    return False

# Score
score = 0

# to keep our window up and running we have to have to create a while loop.
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # Loop through entire events in pygame.
    for event in pygame.event.get():
        # check if event type is QUIT.
        if (event.type == pygame.QUIT):
            running = False

        # check for keystroke(Press) .
        if (event.type == pygame.KEYDOWN):
            # print("A KEY HAS BEEN PRESSED")
            if (event.key == pygame.K_LEFT):
                playerX_change = -5
            if (event.key == pygame.K_RIGHT):
                playerX_change = 5
            if (event.key == pygame.K_SPACE):
                # fire a bullet only on being in ready state.
                if (bullet_state is "ready"):
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if (event.type == pygame.KEYUP):
            playerX_change = 0

    playerX += playerX_change
    # Restrict movement to window size.
    if (playerX <= 0):
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement.
    for i in range(no_of_enemies):
        enemyX[i] += enemyX_change[i]

        if (enemyX[i] <= 0):
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]

        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        if (collision(enemyX[i], enemyY[i], bulletX, bulletY)):
            bullet_state = "ready"
            bulletY = 500
            score += 1
            print(score)
            # 735 as we reset on values greater than 736.
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(20, 100)

        enemy(enemyX[i], enemyY[i],i)

    # BULLET MOVEMENT.
    if (bulletY <= 0):
        bullet_state = "ready"
        bulletY = 500

    # BULLET STATE.
    if (bullet_state is "fire"):
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)

    pygame.display.update()

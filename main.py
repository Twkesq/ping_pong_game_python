from pygame import *
import sys
from random import randint

init()
bgColor = (192, 250, 253)
main_win = display.set_mode((700, 500))
display.set_caption("Ping Pong")
main_win.fill(bgColor)
clock = time.Clock()
font.init()
font1 = font.Font(None, 30)

count1 = 0
count2 = 0


# ------------------------------------------------------------------------------------

def showEndWindow(window, message):
    font.init()
    textWindow = font.Font(None, 70).render(message, True, (255, 255, 255))
    while True:
        # обробка подій
        for el in event.get():
            if el.type == QUIT:
                sys.exit()

        # рендер
        window.blit(textWindow, (250, 250))
        display.update()
        clock.tick(60)


# --------------------------------------------------------------------------------------

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__()
        self.speed = speed
        self.player_image = transform.scale(image.load(player_image), (size_w, size_h))
        self.rect = self.player_image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed

        if keys[K_s]:
            self.rect.y += self.speed


class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed

        if keys[K_DOWN]:
            self.rect.y += self.speed


player1 = Player1("platform.png", 60, 250, 3, 50, 100)
player2 = Player2("platform.png", 640, 250, 3, 50, 100)


class Ball(GameSprite):

    def __init__(self, player_image, x, y, speed, size_w, size_h, b_speed):
        super().__init__(player_image, x, y, speed, size_w, size_h)
        self.b_speed = b_speed

    def update(self):
        global count2
        global count1
        self.rect.x += self.speed
        self.rect.y += self.b_speed
        if ball.rect.colliderect(player1.rect):
            self.speed = self.speed * (-1)

        if ball.rect.colliderect(player2.rect):
            self.speed = self.speed * (-1)

        if self.rect.x < 0:
            count2 += 1
            self.rect.x = 250
            self.rect.y = 250

        if self.rect.x > 700:
            count1 += 1
            self.rect.x = 250
            self.rect.y = 250

        if self.rect.y < 0:
            self.b_speed = self.b_speed * (-1)
            # self.rect.x -= 1
            # self.rect.y -= 1

        if self.rect.y >= 450:
            self.b_speed = self.b_speed * (-1)

            # self.rect.x -= 1
            # self.rect.y -= 1


ball = Ball("ball.png", 250, 250, 3, 50, 50, randint(3, 6))

while True:
    main_win.fill(bgColor)
    player1.draw(main_win)
    player2.draw(main_win)
    ball.draw(main_win)

    text = font1.render("First Player: " + str(count1), False, (255, 0, 0))
    text1 = font1.render("Second Player: " + str(count2), False, (0, 0, 255))

    main_win.blit(text, [20, 40])
    main_win.blit(text1, [500, 40])
    # обробка подій
    for e in event.get():
        if e.type == QUIT:
            sys.exit()

    player1.update()
    player2.update()
    ball.update()
    display.update()
    clock.tick(60)

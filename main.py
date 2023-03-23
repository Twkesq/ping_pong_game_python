from pygame import *
import sys

init()
bgColor = (192, 250, 253)
main_win = display.set_mode((700, 500))
display.set_caption("Ping Pong")
main_win.fill(bgColor)
clock = time.Clock()


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
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        if ball.rect.colliderect(player1.rect):
            self.speed = self.speed * (-1)
            self.rect.x -= 1
            self.rect.y -= 1
        if ball.rect.colliderect(player2.rect):
            self.speed = self.speed * (-1)
            self.rect.x -= 1
            self.rect.y -= 1

        if self.rect.x < 0:
            sys.exit()
        if self.rect.x > 700:
            sys.exit()

        if self.rect.y < 50:
            self.speed = self.speed * (-1)
            self.rect.x -= 1
            self.rect.y -= 1
        if self.rect.y >= 450:
            self.speed = self.speed * (-1)
            self.rect.x -= 1
            self.rect.y -= 1


ball = Ball("ball.png", 250, 250, 3, 50, 50)

while True:
    main_win.fill(bgColor)
    player1.draw(main_win)
    player2.draw(main_win)
    ball.draw(main_win)
    # обробка подій
    for e in event.get():
        if e.type == QUIT:
            sys.exit()

    player1.update()
    player2.update()
    ball.update()
    display.update()
    clock.tick(60)

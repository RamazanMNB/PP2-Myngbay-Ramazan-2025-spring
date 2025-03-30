import pygame, sys
from pygame.locals import *
import random, time

# инициализация pygame
pygame.init()

# фпс (чтобы игра шла плавно)
fps = 60  
frame_per_sec = pygame.time.Clock()

# цвета (чтобы не писать их каждый раз)
black = (0, 0, 0)
white = (255, 255, 255)

# размеры окна
screen_width = 400
screen_height = 600

# переменные для игры
speed = 5  # скорость врагов
score = 0  # счёт за избегание машин
coins_collected = 0  # количество собранных монет

# шрифты (для вывода текста)
font = pygame.font.SysFont("verdana", 60)
font_small = pygame.font.SysFont("verdana", 20)
game_over = font.render("game over", True, black)

# загружаем фон
background = pygame.image.load("Animatedstreet.png")

# создаём окно
displaysurf = pygame.display.set_mode((screen_width, screen_height))
displaysurf.fill(white)
pygame.display.set_caption("гта 6") 


# класс врага (машина, которая едет на игрока)
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")  # загружаем картинку машины
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)  # рандомное появление сверху

    def move(self):
        global score
        self.rect.move_ip(0, speed)  # машина едет вниз
        if self.rect.bottom > screen_height:  # если вышла за экран
            score += 1  # увеличиваем счёт
            self.rect.top = 0  # возвращаем её наверх
            self.rect.center = (random.randint(40, screen_width - 40), 0)  # новая случайная позиция


# класс игрока (машина, которой мы управляем)
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")  # загружаем картинку игрока
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  # стартовая позиция

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # узнаём, какие кнопки нажаты
        if self.rect.left > 0 and pressed_keys[K_LEFT]:  # если нажата влево
            self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width and pressed_keys[K_RIGHT]:  # если вправо
            self.rect.move_ip(5, 0)


# класс монеты (чтобы собирать очки)
class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.reset_coin()  # метод, который создаёт монету

    def reset_coin(self):
        """случайный размер монеты"""
        if random.choice([True, False]):  
            self.image = pygame.image.load("coin.png")
            self.image = pygame.transform.scale(self.image, (30, 30))  # обычная монета
            self.weight = 1  # даёт 1 очко
        else:
            self.image = pygame.image.load("coin.png")
            self.image = pygame.transform.scale(self.image, (40, 40))  # большая монета
            self.weight = 3  # даёт 3 очка

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), random.randint(-200, -50))  # спавнится сверху

    def move(self):
        global coins_collected
        self.rect.move_ip(0, speed // 2)  # двигается вниз, но медленнее врагов

        # если игрок собрал монету
        if self.rect.colliderect(p1.rect):
            coins_collected += self.weight
            self.reset_coin()  # создаём новую монету

        # если монета ушла вниз, пересоздаём её
        if self.rect.top > screen_height:
            self.reset_coin()


# создаём объекты игрока, врага и монеты
p1 = player()
e1 = enemy()
c1 = coin()

# группы спрайтов (чтобы удобнее работать с объектами)
enemies = pygame.sprite.Group()
enemies.add(e1)

coins = pygame.sprite.Group()
coins.add(c1)

all_sprites = pygame.sprite.Group()
all_sprites.add(p1, e1, c1)

# событие увеличения скорости (чтобы игра усложнялась)
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)  # каждую секунду враги становятся быстрее

# основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.5  # делаем врагов быстрее
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # рисуем фон
    displaysurf.blit(background, (0, 0))

    # выводим счёт и монеты
    score_text = font_small.render(f"score: {score}", True, black)
    coin_text = font_small.render(f"coins: {coins_collected}", True, black)
    displaysurf.blit(score_text, (10, 10))
    displaysurf.blit(coin_text, (screen_width - 100, 10))

    # двигаем и рисуем все объекты
    for entity in all_sprites:
        entity.move()
        displaysurf.blit(entity.image, entity.rect)

    # проверяем, врезался ли игрок во врага
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound('crash.wav').play()  # звук аварии
        time.sleep(1)

        # экран "game over"
        displaysurf.fill((255, 0, 0))
        displaysurf.blit(game_over, (30, 250))

        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    frame_per_sec.tick(fps)  # ограничиваем фпс, чтобы игра не лагала

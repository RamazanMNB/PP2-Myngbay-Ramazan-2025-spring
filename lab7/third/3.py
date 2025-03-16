import pygame
import sys

pygame.init()


screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("red circle")


WHITE = (255, 255, 255)


x, y = 100, 100  

speed = 20

running = True
while running:
    screen.fill(WHITE)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x - 25 - speed >= 0:  # Левая граница
            x -= speed
    if keys[pygame.K_RIGHT]:
        if x + 25 + speed <= screen_width:  # Правая граница
            x += speed
    if keys[pygame.K_UP]:
        if y - 25 - speed >= 0:  # Верхняя граница
            y -= speed
    if keys[pygame.K_DOWN]:
        if y + 25 + speed <= screen_height:  # Нижняя граница
            y += speed

    
    pygame.draw.circle(screen, 'red', (x,y), 25)
    pygame.display.update()

pygame.quit()
sys.exit()
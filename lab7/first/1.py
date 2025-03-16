import pygame
from datetime import datetime, timedelta

pygame.init()
img= pygame.image.load('clock.png')
sec= pygame.image.load("sec.png")
min= pygame.image.load("min.png")

screen = pygame.display.set_mode((800,600))

center = (800 // 2, 600 // 2)


run=True
while run:
    
    secund=int(datetime.now().strftime("%S"))
    minut=int(datetime.now().strftime("%M"))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()

    cur_min=-6*minut-53

    cur_sec=-6*secund+60
    
    
    rotsec=pygame.transform.rotate(sec, cur_sec)
    rotmin=pygame.transform.rotate(min, cur_min)
    
    sec_rect = rotsec.get_rect(center=center)
    min_rect = rotmin.get_rect(center=center)

    screen.fill('white')
    screen.blit(img, (0, 0))
    screen.blit(rotsec, sec_rect)
    screen.blit(rotmin, min_rect)

    
    pygame.display.update()



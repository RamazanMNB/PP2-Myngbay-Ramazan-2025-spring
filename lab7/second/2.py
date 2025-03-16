import pygame
import sys
import os
import re

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("СПОТИФАЙ")

pygame.display.flip()

phon= pygame.transform.scale(pygame.image.load('images\po.png'), (800, 600))
pause = pygame.transform.scale(pygame.image.load('images\pause.png'), (100, 100))
play = pygame.transform.scale(pygame.image.load('images\play.png'), (100, 100))
left = pygame.transform.scale(pygame.image.load('images\left.png'), (100, 100))
right = pygame.transform.scale(pygame.image.load('images\sledushii.png'), (100, 100))

leftsmall = pygame.transform.scale(pygame.image.load('images\left.png'), (90, 90))
rightsmall = pygame.transform.scale(pygame.image.load('images\sledushii.png'), (90, 90))


icon = pygame.image.load('images\spotic.png')
pygame.display.set_icon(icon)


music_folder = 'music'  
tracks = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]                #<- мы вводим файл с музыкой
current_track = 0

def play_music():
    pygame.mixer.music.load(os.path.join(music_folder, tracks[current_track]))
    pygame.mixer.music.play()
    

def stop_music():
    pygame.mixer.music.stop()
    

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(tracks)
    play_music()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(tracks)
    play_music()



play_music()
is_play=0
running = True
while running:
    
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:       # Начать
                play_music()
                is_play=0
            elif event.key == pygame.K_2:     # выкл
                pause_music()
                is_play=1
            elif event.key == pygame.K_3:     # вкл
                unpause_music()
                is_play=0
            elif event.key == pygame.K_RIGHT:     # Следующий
                next_track()
                
                
            elif event.key == pygame.K_LEFT:     # Предыдущий
                previous_track()
                
                
            elif event.key == pygame.K_4:     # Стоп
                stop_music()
                is_play=1
            elif event.key == pygame.K_ESCAPE:  # Выход
                running = False
    screen.blit(phon,(0,-100))
    if is_play == 0:
        screen.blit(pause,(345,400))
    else:
        screen.blit(play,(345,400))
    
    screen.blit(left,(100,400))
    screen.blit(right,(600,400))
    pygame.display.update()
pygame.quit()
sys.exit()

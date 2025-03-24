import pygame
import random 

pygame.init()
cell_size = 10

screen = pygame.display.set_mode((300,200))
pygame.display.set_caption("Snake game")

snake = [(50, 50), (40, 50), (30, 50)]
snake_dir = (cell_size, 0)
food = (random.randint(0, (300 - cell_size) // cell_size) * cell_size, 
        random.randint(0, (200 - cell_size) // cell_size) * cell_size)
def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen,(0,255,0), (*segment, cell_size, cell_size))

def draw_food():
    pygame.draw.rect(screen, (255,0,0), (*food, cell_size, cell_size))

running = True 
score_apples = 0

clock = pygame.time.Clock()

while running :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0,cell_size):
                snake_dir = (0, -cell_size)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -cell_size):
                snake_dir = (0, cell_size)
            elif event.key == pygame.K_LEFT and snake_dir != (cell_size, 0):
                snake_dir = (-cell_size, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-cell_size, 0):
                snake_dir = (cell_size, 0)

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)
    if new_head == food:
        score_apples += 1
        food = (random.randint(0, (300 - cell_size) // cell_size) * cell_size, 
        random.randint(0, (200 - cell_size) // cell_size) * cell_size)

    else:
        snake.pop()
    
    if (new_head[0] < 0 or new_head[0] >= 300 or new_head[1] < 0 or new_head[1] >= 200 or new_head in snake[1:]):
        running = False 
    
    screen.fill((0, 0, 0))
    draw_snake()
    draw_food()
  
    pygame.display.flip()
    clock.tick(5)
print(score_apples)
pygame.quit()
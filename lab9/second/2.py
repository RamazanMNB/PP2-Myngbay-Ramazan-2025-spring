import pygame
import random 

pygame.init()

# размер одной клетки
cell_size = 10

#shrift
font_small = pygame.font.SysFont("verdana", 20)


# создаём окно игры
screen = pygame.display.set_mode((300,200))
pygame.display.set_caption("snake game")

# начальная позиция змейки (три сегмента)
snake = [(50, 50), (40, 50), (30, 50)]
snake_dir = (cell_size, 0)  # направление змейки (вправо)

# начальные параметры еды
food = None
food_timer = 0  # таймер для удаления еды
food_weight = 1  # очки за еду

# функция для создания новой еды
def spawn_food():
    global food, food_weight, food_timer
    food = (random.randint(0, (300 - cell_size) // cell_size) * cell_size, 
            random.randint(0, (200 - cell_size) // cell_size) * cell_size)
    
    # 20% шанс получить редкую еду, которая даёт больше очков
    food_weight = 3 if random.random() < 0.2 else 1
    food_timer = 50  # еда исчезает через 50 тактов (примерно 10 секунд)

# вызываем функцию, чтобы сразу появилась первая еда
spawn_food()

# функция рисования змейки
def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, (0,255,0), (*segment, cell_size, cell_size))

# функция рисования еды
def draw_food():
    if food:  # рисуем еду только если она есть
        color = (255, 255, 0) if food_weight == 3 else (255, 0, 0)  # редкая еда - жёлтая
        pygame.draw.rect(screen, color, (*food, cell_size, cell_size))

running = True 
score_apples = 0  # счётчик очков
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, cell_size):
                snake_dir = (0, -cell_size)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -cell_size):
                snake_dir = (0, cell_size)
            elif event.key == pygame.K_LEFT and snake_dir != (cell_size, 0):
                snake_dir = (-cell_size, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-cell_size, 0):
                snake_dir = (cell_size, 0)

    # двигаем змейку
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # проверяем, съела ли змейка еду
    if new_head == food:
        score_apples += food_weight  # прибавляем очки в зависимости от веса еды
        spawn_food()  # создаём новую еду
    else:
        snake.pop()  # если еду не съели, убираем последний сегмент

    # уменьшаем таймер еды, если он есть
    if food_timer > 0:
        food_timer -= 1
    if food_timer == 0:
        spawn_food()  # если таймер кончился, создаём новую еду

    # проверяем столкновения со стенами или с самой собой
    if (new_head[0] < 0 or new_head[0] >= 300 or 
        new_head[1] < 0 or new_head[1] >= 200 or 
        new_head in snake[1:]):
        running = False 

    score_text = font_small.render(f"score: {score_apples}", True, 'white')
    

    # отрисовка экрана
    screen.fill((0, 0, 0))
    score_text = font_small.render(f"score: {score_apples}", True, 'white')
    screen.blit(score_text, (10, 10))
    draw_snake()
    draw_food()

    pygame.display.flip()
    clock.tick(5)  # ограничение фпс (скорости игры)

# выводим счёт после окончания игры
print("score:", score_apples)
pygame.quit()
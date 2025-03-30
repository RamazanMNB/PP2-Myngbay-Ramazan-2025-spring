import sys
import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drawing")


tool = "line"
color = BLACK
draw = False
shapes = []

# функция отрисовки фигур
def draw_shape(surface, shape):
    tool,color,start,end = shape


    if tool=="line":
        pygame.draw.line(surface, color, start, end, 3)
    elif tool=="square":
        size=min(abs(end[0] - start[0]), abs(end[1] - start[1]))
        rect=pygame.Rect(start, (size, size))
        pygame.draw.rect(surface, color, rect, 3)
    elif tool=="right_triangle":
        pygame.draw.polygon(surface, color, [start, (start[0], end[1]), end], 3)
    elif tool=="equilateral_triangle":
        height=abs(end[1] - start[1])
        pygame.draw.polygon(surface, color, [start, (start[0] - height, end[1]), (start[0] + height, end[1])], 3)
    elif tool=="rhombus":
        width=abs(end[0] - start[0])
        height=abs(end[1] - start[1])
        pygame.draw.polygon(surface, color, [(start[0], start[1] - height // 2), (start[0] - width // 2, start[1]),
                                             (start[0], start[1] + height // 2), (start[0] + width // 2, start[1])], 3)
    elif tool=="circle":
        radius=max(abs(end[0] - start[0]), abs(end[1] - start[1]))
        pygame.draw.circle(surface, color, start, radius, 3)

# мэйн функция

def main():
    global tool, color, draw

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    tool = "line"
                elif event.key == pygame.K_s:
                    tool = "square"
                elif event.key == pygame.K_t:
                    tool = "right_triangle"
                elif event.key == pygame.K_e:
                    tool = "equilateral_triangle"
                elif event.key == pygame.K_h:
                    tool = "rhombus"
                elif event.key == pygame.K_c:
                    tool = "circle"
                elif event.key == pygame.K_r:
                    color = (255, 0, 0)  # кр
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)  # зел
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)  # син
                elif event.key == pygame.K_q:
                    shapes.clear()  # очистить
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # лкм
                    draw = True
                    start_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    draw = False
                    end_pos = event.pos
                    shapes.append((tool, color, start_pos, end_pos))

        # рисовка всех сохранённых фигур
        for shape in shapes:
            draw_shape(screen, shape)

        # Временный предварительный просмотр фигуры во время рисования
        if draw:
            end_pos = pygame.mouse.get_pos()
            draw_shape(screen, (tool, color, start_pos, end_pos))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


import pygame
import numpy as np

# 定义参数
cell_size = 10  # 细胞大小
width, height = 1280, 800  # 窗口尺寸
cols, rows = width // cell_size, height // cell_size  # 列数和行数

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

# 创建初始网格（随机）
grid = np.random.choice([0, 1], size=(rows, cols), p=[0.8, 0.2])
iteration = 0  # 迭代计数器

def draw_grid():
    """绘制细胞网格"""
    for y in range(rows):
        for x in range(cols):
            color = (255, 255, 255) if grid[y, x] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size - 1, cell_size - 1))

def update_grid():
    """更新网格到下一代"""
    global grid, iteration
    new_grid = grid.copy()
    for y in range(rows):
        for x in range(cols):
            total = int((np.sum(grid[max(y-1, 0):min(y+2, rows), max(x-1, 0):min(x+2, cols)]) - grid[y, x]))
            if grid[y, x] == 1:
                if (total < 2) or (total > 3):
                    new_grid[y, x] = 0
            else:
                if total == 3:
                    new_grid[y, x] = 1
    grid = new_grid
    iteration += 1

def draw_iteration():
    """绘制迭代次数"""
    font = pygame.font.Font(None, 36)  # 使用默认字体，字号为36
    text = font.render(f'Iteration: {iteration}', True, (255, 255, 255))  # 白色文字
    screen.blit(text, (10, 10))  # 在屏幕左上角显示文字

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_grid()
        draw_iteration()  # 绘制迭代次数
        update_grid()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(10)  # 控制帧率
    pygame.quit()

if __name__ == '__main__':
    main()
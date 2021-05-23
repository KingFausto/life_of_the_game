import pygame
import random

"""Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction."""


def create_grid(rows, cols):
    return [[random.randint(0, 1) for i in range(rows)] for j in range(cols)]


def update(y, x, grid):
    live_neighbors = grid[y][x] * -1

    for j in range(-1, 2):
        for i in range(-1, 2):
            if grid[(y+j) % len(grid)][(x+i) % len(grid)] == 1:
                live_neighbors += 1

    if grid[y][x] == 1 and live_neighbors in [2, 3]:
        return 1
    elif grid[y][x] == 0 and live_neighbors == 3:
        return 1
    else:
        return 0


def main():
    pygame.init()

    size = width, height = 600, 600
    scale = 5

    pygame.display.set_caption("Game of Life")
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    rows = width//scale
    cols = height//scale

    next_grid = create_grid(rows, cols)

    while True:
        clock.tick(30)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        grid = next_grid
        next_grid = [[0 for i in range(rows)] for j in range(cols)]

        for j in range(cols):
            for i in range(rows):
                # draw
                rect = i*scale, j*scale, scale, scale
                if grid[j][i] == 1:
                    pygame.draw.rect(window, (0, 0, 0), rect)

                # next generation
                next_grid[j][i] = update(j, i, grid)

        pygame.display.update()
        window.fill((255, 255, 255))


if __name__ == "__main__":
    main()

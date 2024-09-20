import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
FPS = 10

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Классы
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Stick:
    def __init__(self):
        self.blocks = [Block(5, 0), Block(5, 1), Block(5, 2), Block(5, 3)]
        self.color = RED

    def draw(self, surface):
        for block in self.blocks:
            pygame.draw.rect(
                surface,
                self.color,
                (block.x * BLOCK_SIZE, block.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            )

    def move_down(self):
        for block in self.blocks:
            block.y += 1

    def move_left(self):
        for block in self.blocks:
            block.x -= 1

    def move_right(self):
        for block in self.blocks:
            block.x += 1

# Функции
def draw_grid(surface):
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(surface, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(surface, WHITE, (0, y), (SCREEN_WIDTH, y))

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Тетрис")
    clock = pygame.time.Clock()

    stick = Stick()

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    stick.move_left()
                elif event.key == pygame.K_RIGHT:
                    stick.move_right()
                elif event.key == pygame.K_DOWN:
                    stick.move_down()

        stick.move_down()
        stick.draw(screen)
        draw_grid(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
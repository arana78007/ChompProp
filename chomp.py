import pygame
import sys

pygame.init()

# Set up display
WIDTH, HEIGHT = 300, 200
ROWS, COLS = 4, 4  
SQUARE_SIZE = WIDTH // COLS  # Size of each square
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chomp Game")


WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Game state
grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]  # 1 represents a chocolate piece, 0 is chomped
game_over = False

# Function to draw the grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:  
                pygame.draw.rect(screen, BROWN, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
            else:  
                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)


def chomp(row, col):
    for r in range(row, ROWS):
        for c in range(col, COLS):
            grid[r][c] = 0  # Chomp all squares below and to the right


running = True
while running:
    screen.fill(WHITE)  
    
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE
            
            if grid[row][col] == 1:
                chomp(row, col)
                
                if grid[0][0] == 0:
                    print("Game over! Poisoned square chomped.")
                    game_over = True

    pygame.display.flip()  

pygame.quit()

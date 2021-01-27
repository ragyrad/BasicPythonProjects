import pygame as pg
from enum import Enum

WIDTH = 800
HEIGHT = 600
FPS = 60


class Cell(Enum):
    EMPTY = 0
    SNAKE = 1
    SNAKE_HEAD = 2
    FOOD = 3

    def draw_cell(self, window, color, x, y, w, h):
        pg.draw.rect(window, color, (x, y, w, h))


class Board:
    board_cell_size = 20

    def __init__(self, width, height):
        self.cells_wide = width // 20
        self.cells_height = height // 20
        self.board_cells = [[Cell.EMPTY] * self.cells_wide for _ in range(self.cells_height)]
        self.colors = {'black': (0, 0, 0), 'green': (0, 200, 0),'dark green': (0, 100, 0), 'yellow': (255, 250, 124)}

    def draw_board(self, window):
        color = None
        for i in range(self.cells_height):
            for j in range(self.cells_wide):
                cell = self.board_cells[i][j]
                if cell == Cell.EMPTY:
                    color = self.colors['black']
                elif cell == Cell.SNAKE:
                    color = self.colors['green']
                elif cell == Cell.SNAKE_HEAD:
                    color = self.colors['dark green']
                elif cell == Cell.FOOD:
                    color = self.colors['yellow']
                if color:
                    cell.draw_cell(window, color, j * self.board_cell_size,
                                                  i * self.board_cell_size,
                                                  self.board_cell_size,
                                                  self.board_cell_size)

    def get_board(self):
        return self.board_cells

    def get_board_size(self):
        return self.cells_wide, self.cells_height


class Snake:
    start_game_length = 5

    def __init__(self):
        self.length =  self.start_game_length
        self.speed = self.length
        self.snake_coords = []

    def create_snake_coords(self, board_width, board_height):
        center_x = board_width // 2
        center_y = board_height // 2
        for i in range(self.length):
            if i:
                self.snake_coords.append([center_y, center_x - i])
            else:
                self.snake_coords.append([center_y, center_x])

    def draw_snake(self, board):
        for i in range(len(self.snake_coords)):
            y, x = self.snake_coords[i]
            if i == 0:
                board.board_cells[y][x] = Cell.SNAKE_HEAD
            else:
                board.board_cells[y][x] = Cell.SNAKE

    def move_snake(self, board):
        pass


class GameManager:
    def __init__(self, width, height, fps):
        pg.init()
        self.clock = pg.time.Clock()
        self.running = True
        self.window = pg.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.fps = fps

    def main_loop(self):
        """Main loop and basic game logic"""
        board = Board(self.width, self.height)
        board_width, board_height = board.get_board_size()
        snake = Snake()
        snake.create_snake_coords(board_width, board_height)

        while self.running:
            self.clock.tick(self.fps)
            # Event handler
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        print("move up")
                    if event.key == pg.K_DOWN:
                        print("move down")
                    if event.key == pg.K_LEFT:
                        print("move left")
                    if event.key == pg.K_RIGHT:
                        print("move right")

                if event.type == pg.QUIT:
                    self.running = False

            board.draw_board(self.window)
            board_cells = board.get_board()
            snake.draw_snake(board)
            pg.display.flip()

        # End main loop
        pg.quit()


gm = GameManager(WIDTH, HEIGHT, FPS)
gm.main_loop()
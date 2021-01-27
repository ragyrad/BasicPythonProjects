from random import randint
import pygame as pg
from enum import Enum

WIDTH = 1600
HEIGHT = 900
FPS = 30


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
        self.cells_wide = width // self.board_cell_size
        self.cells_height = height // self.board_cell_size
        self.board_cells = [[Cell.EMPTY] * self.cells_wide for _ in range(self.cells_height)]
        self.colors = {'black': (0, 0, 0), 'green': (0, 200, 0),'dark green': (0, 100, 0), 'yellow': (255, 250, 124)}

    def update_board(self,window):
        self.board_cells = [[Cell.EMPTY] * self.cells_wide for _ in range(self.cells_height)]
        for i in range(self.cells_height):
            for j in range(self.cells_wide):
                color = self.colors['black']
                cell = self.board_cells[i][j]
                cell.draw_cell(window, color, j * self.board_cell_size,
                               i * self.board_cell_size,
                               self.board_cell_size,
                               self.board_cell_size)

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


class Food:
    def __init__(self):
        self.food_coords = None
        self.food_is_exist = False

    def is_exist(self):
        return self.food_is_exist

    def create_food(self, board_w, board_h):
        if not self.food_is_exist:
            self.food_coords = [randint(0, board_h - 1), randint(0, board_w - 1)]
            self.food_is_exist = True

    def draw_food(self, board):
        if self.food_coords:
            y, x = self.food_coords
            board.board_cells[y][x] = Cell.FOOD


class Snake:
    start_snake_len = 5

    def __init__(self):
        self.length =  self.start_snake_len
        self.speed = 1
        self.snake_coords = []

    def create_snake_coords(self, board_width, board_height):
        center_x = board_width // 2
        center_y = board_height // 2
        for i in range(self.length):
            self.snake_coords.append([center_y, center_x - i])

    def draw_snake(self, board):
        for i in range(len(self.snake_coords)):
            y, x = self.snake_coords[i]
            if i == 0:
                board.board_cells[y][x] = Cell.SNAKE_HEAD
            else:
                board.board_cells[y][x] = Cell.SNAKE

    def move_snake(self, direction, board):
        for i in range(1, len(self.snake_coords)):
            y, x = self.snake_coords[-i - 1]
            self.snake_coords[-i] = [y, x]
            board_width, board_height = board.get_board_size()

        if direction == 'right':
            y, x = self.snake_coords[0]
            if x >= board_width - 1:
                x = -1
            self.snake_coords[0] = [y, x + self.speed]
        elif direction == 'left':
            y, x = self.snake_coords[0]
            if x <= 0:
                x = board_width
            self.snake_coords[0] = [y, x - self.speed]
        elif direction == 'up':
            y, x = self.snake_coords[0]
            if y <= 0:
                y = board_height
            self.snake_coords[0] = [y - self.speed, x]
        elif direction == 'down':
            y, x = self.snake_coords[0]
            if y >= board_height - 1:
                y = -1
            self.snake_coords[0] = [y + self.speed, x]


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
        snake.draw_snake(board)
        move = None
        food = Food()

        while self.running:
            self.clock.tick(self.fps)
            # Event handler
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        move = "up"
                    if event.key == pg.K_DOWN:
                        move = "down"
                    if event.key == pg.K_LEFT:
                        move = "left"
                    if event.key == pg.K_RIGHT:
                        move = 'right'

                if event.type == pg.QUIT:
                    self.running = False

            if move:
                snake.move_snake(move, board)

            if not food.is_exist():
                food.create_food(board_width, board_height)

            board.update_board(self.window)
            snake.draw_snake(board)
            food.draw_food(board)
            board.draw_board(self.window)
            pg.display.flip()

        # End main loop
        pg.quit()


gm = GameManager(WIDTH, HEIGHT, FPS)
gm.main_loop()
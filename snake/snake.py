import pygame as pg


WIDTH = 800
HEIGHT = 600


class GameManager:
    def __init__(self, width, height):
        pg.init()
        self.clock = pg.time.Clock()
        self.running = True
        self.window = pg.display.set_mode((width, height))
        self.width = width
        self.height = height

    def main_loop(self):
        while self.running:
            self.clock.tick(60)
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

            pg.display.flip()

        #end main loop
        pg.quit()


gm = GameManager(WIDTH, HEIGHT)
gm.main_loop()
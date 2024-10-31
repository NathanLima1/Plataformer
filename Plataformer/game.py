import pygame as pg
import sys
from player import Player
from enemy import Enemy

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60
BACKGROUND_COLOR = (0, 255, 0)
PLAYER_SIZE = 50

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pg.display.set_caption("Teste")

        self.clock = pg.time.Clock()
        self.running = True

        start_x = WINDOW_WIDTH//4 - PLAYER_SIZE//2
        start_y = WINDOW_HEIGHT//2 - PLAYER_SIZE//2
        self.player = Player(start_x, start_y)
        self.enemy = Enemy(start_x + 200, start_y)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.player.handle_keys()
        self.player.apply_gravity()
        self.enemy.enemy_sight()
        self.enemy.walk()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        pg.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pg.quit()
        sys.exit()


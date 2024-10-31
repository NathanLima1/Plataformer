import pygame as pg
import numpy as np

ENEMY_COLOR = (250, 17, 0)
ENEMY_LIFE = 20
ENEMY_ATTACK = 10
ENEMY_SPEED = 3
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_COLOR_SIGHT = (255, 242, 0)
ENEMY_RANGE_SIGHT = 200


class Enemy:
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.low_sight = (self.rect.centerx + ENEMY_RANGE_SIGHT, self.rect.centery + ENEMY_RANGE_SIGHT)
        self.high_sight = (self.rect.centerx + ENEMY_RANGE_SIGHT, self.rect.centery - ENEMY_RANGE_SIGHT)
        self.color = ENEMY_COLOR
        self.color_sight = ENEMY_COLOR_SIGHT
        self.life = ENEMY_LIFE
        #1 = direita, 0 = esquerda
        self.enemy_side = 0
        self.start_x = x


    #calcula o campo de visão do inimigo e obstaculos
    def enemy_sight(self):
        #alcance da visão
        if self.enemy_side:
            self.low_sight = (self.rect.centerx + ENEMY_RANGE_SIGHT, self.rect.centery + ENEMY_RANGE_SIGHT)
            self.high_sight = (self.rect.centerx + ENEMY_RANGE_SIGHT, self.rect.centery - ENEMY_RANGE_SIGHT)
        else:
            self.low_sight = (self.rect.centerx - ENEMY_RANGE_SIGHT, self.rect.centery - ENEMY_RANGE_SIGHT)
            self.high_sight = (self.rect.centerx - ENEMY_RANGE_SIGHT, self.rect.centery + ENEMY_RANGE_SIGHT)

    def walk(self):
        #movimenta inimigo
        if self.enemy_side:
            self.rect.x += ENEMY_SPEED
        else:
            self.rect.x -= ENEMY_SPEED
        #muda a direção do inimigo pelas coordenadas
        if self.rect.x > self.start_x + 200:
            self.enemy_side = 0
        elif self.rect.x < self.start_x - 200:
            self.enemy_side = 1


    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        pg.draw.line(screen, self.color_sight, self.rect.center, self.low_sight)
        pg.draw.line(screen, self.color_sight, self.rect.center, self.high_sight)
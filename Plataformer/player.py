import pygame as pg


PLAYER_COLOR = (12, 0, 250)
PLAYER_SPEED = 5
PLAYER_LIFE = 50
PLAYER_ATTACK = 10
SWORD_COLOR = (255, 242, 0)
JUMP_STRENGTH = 20
GRAVITY = 1

class Player:
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, 50, 50)
        self.rect_sword = pg.Rect(self.rect.centerx, self.rect.centery, 70, 10)
        self.color = PLAYER_COLOR
        self.life = PLAYER_LIFE
        self.velocity_y = 0
        self.is_jumping = False
        self.second_jump = False
        self.ground_y = y


    def handle_keys(self):
        keys = pg.key.get_pressed()

        # Movimenta o player com AD
        if keys[pg.K_a]:  # Move para a esquerda
            self.rect.x -= PLAYER_SPEED
            self.rect_sword.x -= PLAYER_SPEED
        if keys[pg.K_d]:  # Move para a direita
            self.rect.x += PLAYER_SPEED
            self.rect_sword.x += PLAYER_SPEED
        #Pula e dá segundo pulo
        if keys[pg.K_SPACE]:
            if not self.second_jump and self.is_jumping:
                self.second_jump = True
                self.velocity_y = - JUMP_STRENGTH
            if not self.second_jump and not self.is_jumping:
                self.velocity_y = -JUMP_STRENGTH
                self.is_jumping = True

    def apply_gravity(self):
        # Aplica a gravidade ao player e simula o movimento no eixo Y
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        self.rect_sword.y += self.velocity_y

        # Verifica se o player está no chão e redefine a posição e o estado de pulo
        if self.rect.y >= self.ground_y:
            self.rect.y = self.ground_y
            self.rect_sword.y = self.rect.centery
            self.velocity_y = 0
            self.is_jumping = False
            self.second_jump = False


    def draw(self, screen):
        pg.draw.rect(screen, (0, 0, 0), (0, self.ground_y + 50, 1280, self.ground_y+200))
        pg.draw.rect(screen, self.color, self.rect)
        pg.draw.rect(screen, SWORD_COLOR,self.rect_sword)

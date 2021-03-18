import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("D:\workProject\python\python-demo\images\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        print("飞机中心店",self.center)

    def update(self):
        ship_speed_factor = self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.centerx != 2 * self.screen_rect.centerx:
            self.rect.centerx += ship_speed_factor
        if self.moving_left and self.rect.centerx != 0:
            self.rect.centerx -= ship_speed_factor
        if self.moving_up and self.rect.bottom != 0:
            self.rect.bottom -= ship_speed_factor
        if self.moving_down and self.rect.bottom != self.screen_rect.bottom:
            print("打印下向下高度", self.rect.bottom)
            self.rect.bottom += ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

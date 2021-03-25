import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像，并获取其外接矩形
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

    def update(self):
        ship_speed_factor = self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.centerx + self.rect.width <= self.ai_settings.screen_width:
            self.rect.centerx += ship_speed_factor
        if self.moving_left and self.rect.centerx - self.rect.width >= 0:
            self.rect.centerx -= ship_speed_factor
        if self.moving_up and self.rect.bottom - self.rect.height >= 0:
            self.rect.bottom -= ship_speed_factor
        if self.moving_down and self.rect.bottom != self.screen_rect.bottom:
            self.rect.bottom += ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

import pygame
from pygame.sprite import Sprite
# 单个外星人的类
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        # 初始化外星人并设置其初始位置
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载外星人图像，并获取渲染
        self.image = pygame.image.load("D:\workProject\python\python-demo\images\\alien.bmp");
        self.rect = self.image.get_rect()
        self.width = self.image.get_size()[0]
        self.height = self.image.get_size()[1]
        print("外星人的长宽",self.width,self.height)
        # 每个外星人最初都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 储存外星人的准确位置
        self.x = float(self.rect.x)
    # def update(self):
    #     ship_speed_factor = self.ai_settings.ship_speed_factor
    #     if self.moving_right and self.rect.centerx + self.width <= self.ai_settings.screen_width:
    #         self.rect.centerx += ship_speed_factor
    #     if self.moving_left and self.rect.centerx - self.width >= 0:
    #         self.rect.centerx -= ship_speed_factor
    #     if self.moving_up and self.rect.bottom - self.size[0] >= 0:
    #         self.rect.bottom -= ship_speed_factor
    #     if self.moving_down and self.rect.bottom != self.screen_rect.bottom:
    #         self.rect.bottom += ship_speed_factor

    def blitme(self):
        # 指定位置渲染外星人
        self.screen.blit(self.image, self.rect)

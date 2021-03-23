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
        # 每个外星人最初都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 储存外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        # 指定位置渲染外星人
        self.screen.blit(self.image, self.rect)

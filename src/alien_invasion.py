import pygame
from pygame._sprite import Group

import game_functions as gf
from setting import Settings
from ship import Ship

def run_game():
    # 初始化游戏
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    pygame.display.set_gamma(0, 255, 0)
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()
    ship_height = ship.rect.height
    # 创建外星人群
    gf.create_aliens(ai_setting, screen, aliens, ship_height)
    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        # 子弹管理更新处理
        gf.update_bullets(ai_setting,screen,ship,bullets,aliens)
        gf.update_aliens(ai_setting, aliens)
        gf.update_screen(ai_setting, screen, ship, aliens, bullets)


run_game()

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

    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        # 子弹管理更新处理
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting, screen, ship, bullets)


run_game()

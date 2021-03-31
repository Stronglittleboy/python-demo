import pygame
from pygame._sprite import Group

import game_functions as gf
from setting import Settings
from ship import Ship
from src.button import Button
from src.game_stats import GameStats
from src.scoreboard import Scoreboard


def run_game():
    # 初始化游戏
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_setting, screen, "PLAY")
    pygame.display.set_gamma(0, 255, 0)
    ship = Ship(ai_setting, screen)
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)

    bullets = Group()
    aliens = Group()

    ship_height = ship.rect.height
    # 创建外星人群
    gf.create_aliens(ai_setting, screen, aliens, ship_height)
    while True:
        gf.check_events(ai_setting, screen, stats, play_button, ship, aliens, bullets, sb)
        if stats.game_active:
            ship.update()
            # 子弹管理更新处理
            gf.update_bullets(ai_setting, screen, ship, bullets, aliens, stats, sb)
            # 更新外星人
            gf.update_aliens(ai_setting, screen, ship, stats, aliens, bullets,sb)
        # 刷新窗口
        gf.update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()

import sys
import pygame

from src.alien import Alien
from src.bullet import Bullet


# 监听事件
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down_methods(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            key_up_methods(event, ship)


# 按键放开后方法
def key_up_methods(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


# 按键按下后方法
def key_down_methods(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)
    # 按键Q退出
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, bullets, screen, ship):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_setting, screen, ship, aliens, bullets):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)
    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


# 创建外星人群
def create_aliens(ai_setting, screen, aliens,ship_height):
    alien = Alien(ai_setting, screen)
    # 外星人宽度
    alien_width = alien.rect.width
    # 外星人高度
    alien_height = alien.rect.height

    # 获取一行能容纳外星人的数量
    number_aliens_x = get_number_aliens_x(ai_setting, alien_width)
    # 获取能创建多少行数据
    number_rows = get_number_aliens_y(ai_setting, alien_height, ship_height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, alien_number,row_number, alien_width,alien_height, aliens, screen)


def get_number_aliens_y(ai_setting, alien_height, ship_height):
    # 可容纳外星人的高度
    available_space_y = ai_setting.screen_height - 3 * alien_height - ship_height
    # 获取能容纳外星人的行数
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


# 创建一个外星人并将其加入当前行
def create_alien(ai_setting, alien_number,row_number, alien_width, alien_height,aliens, screen):
    alien = Alien(ai_setting, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2* alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


# 计算每行可容纳多少个外星人
def get_number_aliens_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

import sys
from time import sleep

import pygame

from src.aliengame.alien import Alien
from src.aliengame.bullet import Bullet


# 在玩家单击Play按钮时开始新游戏
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        # 清空外星人列表和子弹系列
        aliens.empty()
        bullets.empty()
        create_aliens(ai_settings, screen, aliens, ship.rect.height)
        ship.center_ship()


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down_methods(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            key_up_methods(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb)


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


def update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)
    ship.blitme()
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(ai_setting, screen, ship, bullets, aliens, stats, sb):
    # 更新子弹位置，并删除已消失的子弹
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中了外星人

    check_bullet_alien_collisions(ai_setting, aliens, bullets, screen, ship, stats, sb)


# 打所有的外星人被消灭后
def check_bullet_alien_collisions(ai_setting, aliens, bullets, screen, ship, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_setting.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()

        # 提升等级
        stats.level += 1
        sb.prep_level()
        ship_height = ship.rect.height
        create_aliens(ai_setting, screen, aliens, ship_height)


# 创建外星人群
def create_aliens(ai_setting, screen, aliens, ship_height):
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
            create_alien(ai_setting, alien_number, row_number, alien_width, alien_height, aliens, screen)


def get_number_aliens_y(ai_setting, alien_height, ship_height):
    # 可容纳外星人的高度
    available_space_y = ai_setting.screen_height - int(3 * alien_height) - int(ship_height)
    # 获取能容纳外星人的行数
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


# 创建一个外星人并将其加入当前行
def create_alien(ai_setting, alien_number, row_number, alien_width, alien_height, aliens, screen):
    alien = Alien(ai_setting, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


# 计算每行可容纳多少个外星人
def get_number_aliens_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


# 改变外星人方向
def change_fleet_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1


# 检查对型边缘
def check_fleet_edges(ai_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break


# 更新外星人
def ship_hit(ai_setting, stats, screen, ship, aliens, bullets, sb):
    # 生命数量-1
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # 更新积分排
        sb.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        create_aliens(ai_setting, screen, aliens, ship.rect.height)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_setting, screen, ship, stats, aliens, bullets, sb):
    # 更新外星人群中所有外星人的位置
    check_fleet_edges(ai_setting, aliens)
    aliens.update()
    check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets, sb)
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, screen, ship, aliens, bullets, sb)


# 检测外星人到底，游戏结束
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break


# 检查是否诞生了新的最高分
def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

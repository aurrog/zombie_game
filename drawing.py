# import pygame.draw
from settings import*


def drawing(screen, wmap, player, zombies, bullets, died, click_pos):
    screen.fill(BLACK)
    for obj in died:
        screen.blit(blood_spot_img, blood_spot_img.get_rect(center=obj))
    for i, j in wmap:
        pygame.draw.rect(screen, (150, 100, 80), (i, j, TILE, TILE))
    for enemy in zombies:
            if enemy.turn == 'up':
                zombie_img = zombie_img_up
            elif enemy.turn == 'down':
                zombie_img = zombie_img_down
            elif enemy.turn == 'left':
                zombie_img = zombie_img_left
            elif enemy.turn == 'right':
                zombie_img = zombie_img_right
            zombie_rect = zombie_img.get_rect(center=enemy.pos)
            screen.blit(zombie_img, zombie_rect)
            pygame.draw.rect(screen, RED, (enemy.x-20, enemy.y+15, 40, 10))
            pygame.draw.rect(screen, GREEN, (enemy.x-20, enemy.y+15, enemy.lives*10, 10))
    if player.select_gun == 'knife':
        if player.turn == 'up':
            player_img = player_with_knife_img_up
        elif player.turn == 'down':
            player_img = player_with_knife_img_down
        elif player.turn == 'left':
            player_img = player_with_knife_img_left
        elif player.turn == 'right':
            player_img = player_with_knife_img_right
    elif player.select_gun == 'shotgun':
        if player.turn == 'up':
            player_img = player_with_shotgun_img_up
        elif player.turn == 'down':
            player_img = player_with_shotgun_img_down
        elif player.turn == 'left':
            player_img = player_with_shotgun_img_left
        elif player.turn == 'right':
            player_img = player_with_shotgun_img_right
    elif player.select_gun == 'gun':
        if player.turn == 'up':
            player_img = player_with_gun_img_up
        elif player.turn == 'down':
            player_img = player_with_gun_img_down
        elif player.turn == 'left':
            player_img = player_with_gun_img_left
        elif player.turn == 'right':
            player_img = player_with_gun_img_right
    elif player.select_gun == 'rifle':
        if player.turn == 'up':
            player_img = player_with_rifle_img_up
        elif player.turn == 'down':
            player_img = player_with_rifle_img_down
        elif player.turn == 'left':
            player_img = player_with_rifle_img_left
        elif player.turn == 'right':
            player_img = player_with_rifle_img_right
    player_rect = player_img.get_rect(center=player.pos)
    screen.blit(player_img, player_rect)

    if player.shotgun_fire_is_see < shotgun_fire_is_see:
        if player.turn == 'up':
            fire_img = shotgun_fire_image_up
            fire_rect = fire_img.get_rect(center=(player.pos[0]+10, player.pos[1]-35))
        elif player.turn == 'down':
            fire_img = shotgun_fire_image_down
            fire_rect = fire_img.get_rect(center=(player.pos[0]-8, player.pos[1] + 35))
        elif player.turn == 'left':
            fire_img = shotgun_fire_image_left
            fire_rect = fire_img.get_rect(center=(player.pos[0]- 35, player.pos[1]-10))
        elif player.turn == 'right':
            fire_img = shotgun_fire_image_right
            fire_rect = fire_img.get_rect(center=(player.pos[0] + 35, player.pos[1] + 10))
        screen.blit(fire_img, fire_rect)

    pygame.draw.rect(screen, (140, 140, 140), (800, 0, 100, 800))

    for i in range(player.lives):
        pygame.draw.rect(screen, RED,
                         (WIDTH-100+live_behind_x+live_side*i+live_behind_x*i, live_y, live_side, live_side))

    for button in buttons_list:
        if button[0] < click_pos[0] < button[0]+button_tile and button[1] < click_pos[1] < button[1]+button_tile:
            player.select_gun = button[2]
        pygame.draw.rect(screen, BLACK, (button[0], button[1], button_tile, button_tile))
        icon_rect = button[3].get_rect(center=(button[0]+1/2*button_tile, button[1]+1/2*button_tile))
        screen.blit(button[3], icon_rect)
        if player.select_gun == button[2]:
            pygame.draw.rect(screen, RED, (button[0], button[1], button_tile, button_tile), 4)
    # for enemy in zombies:
    #     pygame.draw.line(screen, RED, (player.x, player.y), (player.x, enemy.y))
    #     pygame.draw.line(screen, GREEN, (player.x, enemy.y), (enemy.x, enemy.y))
    #     pygame.draw.line(screen, BLUE, (player.x, player.y), (enemy.x, enemy.y))

    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)
        elif bullet.rect.y >= WIDTH:
            bullets.remove(bullet)
        elif bullet.rect.x <= 0:
            bullets.remove(bullet)
        elif bullet.rect.x >= WIDTH:
            bullets.remove(bullet)
    bullets.update()
    player.draw_bullets()
    pygame.display.update()

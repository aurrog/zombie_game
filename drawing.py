from settings import*


def drawing(screen, wmap, player, zombies, bullets, died):
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
            # pygame.draw.circle(screen, (0, 200, 100), enemy.pos, 2)

    if player.turn == 'up':
        player_img = player_with_knife_img_up
    elif player.turn == 'down':
        player_img = player_with_knife_img_down
    elif player.turn == 'left':
        player_img = player_with_knife_img_left
    elif player.turn == 'right':
        player_img = player_with_knife_img_right
    player_rect = player_img.get_rect(center=player.pos)
    screen.blit(player_img, player_rect)
    # pygame.draw.circle(screen, (200, 200, 100), player.pos, 2)


    pygame.draw.rect(screen, (140, 140, 140), (800, 0, 100, 800))

    for i in range(player.lives):
        pygame.draw.rect(screen, RED, (WIDTH-100+live_behind_x+live_side*i+live_behind_x*i, live_y, live_side, live_side))

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

from settings import*


def drawing(screen, map, player, zombie, bullets):
    screen.fill(BLACK)
    for i, j in map:
        pygame.draw.rect(screen, (150, 100, 80), (i, j, TILE, TILE))

    if zombie.turn == 'up':
        zombie_img = zombie_img_up
    elif zombie.turn == 'down':
        zombie_img = zombie_img_down
    elif zombie.turn == 'left':
        zombie_img = zombie_img_left
    elif zombie.turn == 'right':
        zombie_img = zombie_img_right
    zombie_rect = zombie_img.get_rect(center=zombie.pos)
    screen.blit(zombie_img, zombie_rect)

    if player.turn == 'up':
        player_img = player_with_knife_img_up
    elif player.turn == 'down':
        player_img = player_with_knife_img_down
    elif player.turn == 'left':
        player_img = player_with_knife_img_left
    elif player.turn == 'right':
        player_img = player_img_right
    player_rect = player_img.get_rect(center=player.pos)
    screen.blit(player_img, player_rect)

    pygame.draw.circle(screen, (200, 200, 100), player.pos, 10)
    pygame.draw.rect(screen, (140, 140, 140), (800, 0, 100, 800))

    pygame.draw.line(screen, RED, (player.x, player.y), (player.x, zombie.y))
    pygame.draw.line(screen, GREEN, (player.x, zombie.y), (zombie.x, zombie.y))
    pygame.draw.line(screen, BLUE, (player.x, player.y), (zombie.x, zombie.y))

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

import drawing
from settings import *
import map
import classPerson
from pygame.sprite import Group
import zombie
import bfs
import random

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bullets = Group()
player = classPerson.Player(screen, bullets)
zombies = []
died = []
for z in range(5):
    pos = random.choice(zombie_spawn_massive)
    zombies.append(zombie.Zombie(pos[0], pos[1]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.hit_cooldown += 1
    player.shotgun_fire_is_see += 1
    for enemy in zombies:
        enemy.bite_cooldown += 1
        player.lives = enemy.check_bite(player)
    player.movement()

    zombies = player.check_player_attack(zombies)
    for enemy in zombies:
        enemy_x_last, enemy_y_last = enemy.pos
        enemy.x, enemy.y = bfs.character_movement(enemy, player)
        if enemy.x < enemy_x_last:
            enemy.turn = 'left'
        if enemy.x > enemy_x_last:
            enemy.turn = 'right'
        if enemy.y < enemy_y_last:
            enemy.turn = 'up'
        if enemy.y > enemy_y_last:
            enemy.turn = 'down'
    drawing.drawing(screen, map.world_map, player, zombies, bullets, died)
    i = -1
    for z in zombies:
        i += 1
        if not z.is_alive:
            died.append(z.pos)
            zombies.pop(i)

    clock.tick(60)

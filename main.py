import drawing
from settings import *
import map
import classPerson
from pygame.sprite import Group
import zombie
import bfs

# pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bullets = Group()
player = classPerson.Player(screen, bullets)
zombie = zombie.Zombie(750, 750)
mas = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(mas)
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mas.append(pygame.mouse.get_pos())
    player.hit_cooldown += 1
    zombie.bite_cooldown += 1
    player.lives = zombie.check_bite(player)
    player.movement(zombie)
    zombie.lives = player.check_player_attack(zombie)
    zombie_x_last, zombie_y_last = zombie.pos
    zombie.x, zombie.y = bfs.character_movement(zombie, player)
    if zombie.x < zombie_x_last:
        zombie.turn = 'left'
    if zombie.x > zombie_x_last:
        zombie.turn = 'right'
    if zombie.y < zombie_y_last:
        zombie.turn = 'up'
    if zombie.y > zombie_y_last:
        zombie.turn = 'down'
    drawing.drawing(screen, map.world_map, player, zombie, bullets)

    clock.tick(60)

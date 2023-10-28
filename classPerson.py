import map
from settings import *
from bullet import Bullet


class Player:
    def __init__(self, screen, bullets):
        self.screen = screen
        self.speed = player_speed
        self.lives = player_lives
        self.turn = player_start_turn
        self.bullets = bullets
        self.x, self.y = player_start_position
        self.side = player_side
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)
        self.select_gun = player_start_gun
        self.hit_cooldown = player_hit_knife_cooldown

    @property
    def pos(self):
        return self.x, self.y

    @property
    def pos_square(self):
        return self.x//TILE, self.y//TILE

    def detect_collisions(self, dx, dy):
        # print(1)
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(map.collision_walls)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = map.collision_walls[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy

    def bullets_collision(self, walls):
        collision_walls = pygame.sprite.groupcollide(self.bullets, walls, True, True)
        if collision_walls:
            return 1

    # def attack(self, zombie):
    #     if self.select_gun == 'knife':
    #         if abs(zombie.x-self.x) < knife_radius and abs(zombie.y-self.y) < knife_radius:
    #             hit_sound.play()
    #             # return zombie.lives-2
    #         else:
    #             knife_miss_sound.play()
    #             # return zombie.lives


    def movement(self, zombie):
        self.rect.center = self.x, self.y
        keys = pygame.key.get_pressed()
        # self.x += player_speed
        # if self.x > 770:
        #     self.x = 770

        if keys[pygame.K_w]:
            self.turn = 'up'
            if self.y <= TILE / 4:
                self.y = TILE / 4
            else:
                self.detect_collisions(0, self.y - self.y - self.speed)
        if keys[pygame.K_s]:
            self.turn = 'down'
            if self.y >= WIDTH - TILE / 4:
                self.y = WIDTH - TILE / 4
            else:
                self.detect_collisions(0, self.y - self.y + self.speed)
        if keys[pygame.K_a]:
            self.turn = 'left'
            if self.x <= TILE / 4:
                self.x = TILE / 4
            else:
                self.detect_collisions(self.x - self.x - self.speed, 0)
        if keys[pygame.K_d]:
            self.turn = 'right'
            if self.x >= WIDTH - TILE / 4:
                self.x = WIDTH - TILE / 4
            else:
                self.detect_collisions(self.x - self.x + self.speed, 0)

        # if keys[pygame.K_SPACE]:
        #     if self.hit_cooldown >= player_hit_knife_cooldown:
        #         self.hit_cooldown = 0
        #         self.attack(zombie)
        #     # if len(self.bullets) != bullet_allowed:
        #     #     # gun_sound = pygame.mixer.Sound('sounds/byistryiy-perezaryad-obreza.mp3')
        #     #     # gun_sound.play()
        #     #     new_bullet = Bullet(self.screen, player)
        #     #     self.bullets.add(new_bullet)
        #     #     gun_sound = pygame.mixer.Sound('sounds/byistryiy-perezaryad-obreza.mp3')
        #     #     gun_sound.play()

    def check_player_attack(self, zombie):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.hit_cooldown >= player_hit_knife_cooldown:
                self.hit_cooldown = 0
                if self.select_gun == 'knife':
                    if abs(zombie.x - self.x) < knife_radius and abs(zombie.y - self.y) < knife_radius:
                        hit_sound.play()
                        return zombie.lives-knife_damage
                    else:
                        knife_miss_sound.play()
        return zombie.lives
    # def bullet_collision(self, walls, bullet):
    #     collisions = pygame.sprite.groupcollide(self.bullets, walls, True, True)
    #     if collisions != {}:
    #         wp.text_map = self.return_wall_row(bullet_x, bullet_y)
    #         wp.collision_walls = []
    #         wp.world_map = set()
    #         for j, row in enumerate(wp.text_map):
    #             for i, char in enumerate(row):
    #                 if char == '1':
    #                     wp.collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
    #                     wp.world_map.add((i * TILE, j * TILE))

    def draw_bullets(self):
        for bullet in self.bullets.sprites():
            # self.bullet_collision(walls, bullet.rect[0], bullet.rect[1])
            bullet.draw_bullet()

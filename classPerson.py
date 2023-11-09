import pygame

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
        self.knife_hit_cooldown = player_hit_knife_cooldown
        self.shotgun_shot_cooldown = player_shotgun_shot_cooldown
        self.rifle_shot_cooldown = player_rifle_shot_cooldown
        self.gun_shot_cooldown = player_gun_shot_cooldown
        self.shotgun_fire_is_see = shotgun_fire_is_see
        self.shotgun_bullets = shotgun_bullets

    @property
    def pos(self):
        return self.x, self.y

    @property
    def pos_square(self):
        return self.x // TILE, self.y // TILE

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

    def detect_bullets_collision(self, rect, dx, dy):
        next_rect = rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(map.collision_walls)
        if len(hit_indexes):
            print(1)
            return True
    # def bullets_collision(self, walls):
    #     collision_walls = pygame.sprite.groupcollide(self.bullets, walls, True, True)
    #     if collision_walls:
    #         return 1

    # def attack(self, zombie):
    #     if self.select_gun == 'knife':
    #         if abs(zombie.x-self.x) < knife_radius and abs(zombie.y-self.y) < knife_radius:
    #             hit_sound.play()
    #             # return zombie.lives-2
    #         else:
    #             knife_miss_sound.play()
    #             # return zombie.lives

    def movement(self):
        self.rect.center = self.x, self.y
        keys = pygame.key.get_pressed()
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

    def check_player_attack(self, zombies):
        keys = pygame.key.get_pressed()
        lives = [e.lives for e in zombies]
        if keys[pygame.K_SPACE]:
            if self.select_gun == 'knife':
                if self.knife_hit_cooldown >= player_hit_knife_cooldown:
                    self.knife_hit_cooldown = 0
                    for enemy in zombies:
                        if abs(enemy.x - self.x) < knife_radius and abs(enemy.y - self.y) < knife_radius:
                            hit_sound.play()
                            enemy.lives -= knife_damage

                    lives2 = [e.lives for e in zombies]
                    if lives == lives2:
                        knife_miss_sound.play()
            if self.select_gun == 'shotgun':
                if self.shotgun_shot_cooldown >= player_shotgun_shot_cooldown:
                    self.shotgun_shot_cooldown = 0
                    shotgun_sound.play()
                    self.shotgun_fire_is_see = 0
                    self.shotgun_bullets -= 1
                    for enemy in zombies:
                        bullet_rect = pygame.Rect(self.x, self.y, shotgun_range_width, shotgun_range_width)
                        bullet_dx, bullet_dy = 0, 0
                        # if abs(enemy.x - self.x) < 200 and abs(enemy.y - self.y) < 40:
                        #     enemy.lives -= 2
                        if self.turn == 'left':
                            if 0 < self.x - enemy.x < shotgun_range and abs(enemy.y - self.y) < shotgun_range_width:
                                for i in range(abs(self.x - enemy.x)):
                                    bullet_dx -= 1
                                    bullet_dy += 0
                                    if not self.detect_bullets_collision(bullet_rect, bullet_dx, bullet_dy):
                                        enemy.lives -= 2
                                        print(2)
                                        break
                        elif self.turn == 'right':
                            if 0 < enemy.x - self.x < shotgun_range and abs(enemy.y - self.y) < shotgun_range_width:
                                for i in range(abs(self.x - enemy.x)):
                                    bullet_dx += 1
                                    bullet_dy += 0
                                    if not self.detect_bullets_collision(bullet_rect, bullet_dx, bullet_dy):
                                        enemy.lives -= 2
                                        print(2)
                                        break
                        elif self.turn == 'up':
                            if abs(enemy.x - self.x) < shotgun_range_width and 0 < self.y - enemy.y < shotgun_range:
                                for i in range(abs(self.x - enemy.x)):
                                    bullet_dx += 0
                                    bullet_dy -= 1
                                    if not self.detect_bullets_collision(bullet_rect, bullet_dx, bullet_dy):
                                        enemy.lives -= 2
                                        print(2)
                                        break
                        elif self.turn == 'down':
                            if abs(enemy.x - self.x) < shotgun_range_width and 0 < enemy.y - self.y < shotgun_range:
                                for i in range(abs(self.x - enemy.x)):
                                    bullet_dx += 0
                                    bullet_dy += 1
                                    if not self.detect_bullets_collision(bullet_rect, bullet_dx, bullet_dy):
                                        enemy.lives -= 2
                                        print(2)
                                        break
            if self.select_gun == 'rifle':
                if self.rifle_shot_cooldown >= player_rifle_shot_cooldown:
                    self.rifle_shot_cooldown = 0
                    rifle_shot_sound.play()
                    for enemy in zombies:
                        if self.turn == 'left':
                            if 0 < self.x - enemy.x < rifle_range and abs(enemy.y - self.y) < rifle_range_width:
                                enemy.lives -= rifle_damage
                        elif self.turn == 'right':
                            if 0 < enemy.x - self.x < rifle_range and abs(enemy.y - self.y) < rifle_range_width:
                                enemy.lives -= rifle_damage
                        elif self.turn == 'up':
                            if abs(enemy.x - self.x) < rifle_range_width and 0 < self.y - enemy.y < rifle_range:
                                enemy.lives -= rifle_damage
                        elif self.turn == 'down':
                            if abs(enemy.x - self.x) < rifle_range_width and 0 < enemy.y - self.y < rifle_range:
                                enemy.lives -= rifle_damage

            if self.select_gun == 'gun':
                if self.gun_shot_cooldown >= player_gun_shot_cooldown:
                    self.gun_shot_cooldown = 0
                    gun_shot_sound.play()

        return zombies

    # def draw_bullets(self):
    #     for bullet in self.bullets.sprites():
    #         # self.bullet_collision(walls, bullet.rect[0], bullet.rect[1])
    #         bullet.draw_bullet()

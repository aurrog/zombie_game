import pygame

pygame.init()
# screen parameters
WIDTH = 900
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

FPS = 60

# design
TILE = 20
live_side = 20
live_behind_x = 10
live_y = 20

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
BRICK_COLOR = (183, 65, 14)

bullet_allowed = 1
bullet_width = 10
bullet_height = 5
cols = 40
rows = 40

# player
player_lives = 3
player_speed = 2
player_start_position = 100, 750
player_start_turn = 'up'
player_side = 15
player_start_gun = 'shotgun'

# zombie
zombie_start_turn = 'right'
zombie_lives = 4
zombie_speed = 1
zombie_start_position = 750, 750
zombie_bite_cooldown = 60
bite_radius = 25
zombie_spawn_massive = [(275, 749), (747, 752), (746, 672), (128, 661), (369, 660), (657, 673), (520, 533), (744, 556),
                        (743, 426), (733, 257), (742, 120), (755, 50), (618, 120), (344, 195), (244, 207), (117, 102),
                        (43, 44), (47, 217), (50, 273), (64, 440), (308, 513), (425, 498), (432, 578), (342, 576),
                        (276, 578), (234, 513), (128, 503), (153, 654), (376, 655)]

# guns
knife_damage = 4
knife_radius = 35
player_hit_knife_cooldown = 60

player_shotgun_shot_cooldown = 60
shotgun_fire_is_see = 20
shotgun_range = 200
shotgun_range_width = 40
shotgun_bullets = 100

player_rifle_shot_cooldown = 7

player_gun_shot_cooldown = 12


# buttons
knife_button_x, knife_button_y = (810, 80)
knife_button_function = 'knife'

shotgun_button_x, shotgun_button_y = (855, 80)
shotgun_button_function = 'shotgun'

gun_button_x, gun_button_y = (810, 135)
gun_button_function = 'gun'

rifle_button_x, rifle_button_y = (855, 135)
rifle_button_function = 'rifle'

button_tile = 80


# images
zombie_img_right = pygame.image.load('images/zombie_attack_0 (3).png')
zombie_img_up = pygame.transform.rotate(zombie_img_right, 90)
zombie_img_down = pygame.transform.rotate(zombie_img_right, 270)
zombie_img_left = pygame.transform.rotate(zombie_img_right, 180)

player_with_knife_img_right = pygame.image.load('images/player_with_knife.png')
player_with_knife_img_left = pygame.transform.rotate(player_with_knife_img_right, 180)
player_with_knife_img_up = pygame.transform.rotate(player_with_knife_img_right, 90)
player_with_knife_img_down = pygame.transform.rotate(player_with_knife_img_right, 270)

player_with_shotgun_img_right = pygame.image.load('images/survivor-idle_shotgun_0 (1).png')
player_with_shotgun_img_left = pygame.transform.rotate(player_with_shotgun_img_right, 180)
player_with_shotgun_img_up = pygame.transform.rotate(player_with_shotgun_img_right, 90)
player_with_shotgun_img_down = pygame.transform.rotate(player_with_shotgun_img_right, 270)

player_with_gun_img_right = pygame.image.load('images/preview_idle (1).png')
player_with_gun_img_left = pygame.transform.rotate(player_with_gun_img_right, 180)
player_with_gun_img_up = pygame.transform.rotate(player_with_gun_img_right, 90)
player_with_gun_img_down = pygame.transform.rotate(player_with_gun_img_right, 270)

player_with_rifle_img_right = pygame.image.load('images/player_rifle (1).png')
player_with_rifle_img_left = pygame.transform.rotate(player_with_rifle_img_right, 180)
player_with_rifle_img_up = pygame.transform.rotate(player_with_rifle_img_right, 90)
player_with_rifle_img_down = pygame.transform.rotate(player_with_rifle_img_right, 270)

shotgun_fire_image_right = pygame.image.load('images/pixil-frame-0 (13).png')
shotgun_fire_image_left = pygame.transform.rotate(shotgun_fire_image_right, 180)
shotgun_fire_image_up = pygame.transform.rotate(shotgun_fire_image_right, 90)
shotgun_fire_image_down = pygame.transform.rotate(shotgun_fire_image_right, 270)

shotgun_icon_img = pygame.image.load('images/free-icon-shotgun-5018824.png')
rifle_icon_img = pygame.image.load('images/free-icon-rifle-238503.png')
gun_icon_img = pygame.image.load('images/free-icon-gun-1320476.png')
knife_icon_img = pygame.image.load('images/free-icon-knife-7661290.png')

blood_spot_img = pygame.image.load('images/pixil-frame-0 (12).png')


# sounds
shotgun_sound = pygame.mixer.Sound('sounds/byistryiy-perezaryad-obreza.mp3')
zombie_sound = pygame.mixer.Sound('sounds/inecraft_zombie_.mp3')
hit_sound = pygame.mixer.Sound('sounds/tupoy-udar-kirpichom-razdavivishiy-sliznyaka.mp3')
knife_miss_sound = pygame.mixer.Sound('sounds/moschnyiy-udar-po-vozduhu.mp3')
player_wound_sound = pygame.mixer.Sound('sounds/mujskoy-vopl-posle-raneniya.mp3')
zombie_attack_sound = pygame.mixer.Sound('sounds/udar-priglushennyiy-reshitelnyiy.mp3')
rifle_shot_sound = pygame.mixer.Sound('sounds/vyistrelyi-iz-avtomata-i-perezaryadka (mp3cut.net).mp3')
gun_shot_sound = pygame.mixer.Sound('sounds/shumnyiy-odinochnyiy-vyistrel.mp3')


buttons_list = [[810, 80, 'knife', knife_icon_img], [810, 180, 'shotgun', shotgun_icon_img], [810, 280, 'gun', gun_icon_img], [810, 380, 'rifle', rifle_icon_img]]

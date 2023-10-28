import pygame


pygame.init()
# screen parameters
WIDTH = 900
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

FPS = 60

TILE = 20


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


# zombie
zombie_start_turn = 'right'
zombie_lives = 5
zombie_speed = 1
zombie_start_position = 750, 750

after_bullets = 60


# images
zombie_img_right = pygame.image.load('../zombie_game/zombie_game/images/zombie_attack_0 (3).png')
zombie_img_up = pygame.transform.rotate(zombie_img_right, 90)
zombie_img_down = pygame.transform.rotate(zombie_img_right, 270)
zombie_img_left = pygame.transform.rotate(zombie_img_right, 180)

player_with_knife_img_right = pygame.image.load('../zombie_game/zombie_game/images/player_with_knife.png')
player_with_knife_img_right.set_colorkey((255, 255, 255))
player_with_knife_img_left = pygame.transform.rotate(player_with_knife_img_right, 180)
player_with_knife_img_up = pygame.transform.rotate(player_with_knife_img_right, 90)
player_with_knife_img_down = pygame.transform.rotate(player_with_knife_img_right, 270)


# sounds
shotgun_sound = pygame.mixer.Sound('../zombie_game/zombie_game/sounds/byistryiy-perezaryad-obreza.mp3')
zombie_sound = pygame.mixer.Sound('../zombie_game/zombie_game/sounds/inecraft_zombie_.mp3')
hit_sound = pygame.mixer.Sound('../zombie_game/zombie_game/sounds/tupoy-udar-kirpichom-razdavivishiy-sliznyaka.mp3')


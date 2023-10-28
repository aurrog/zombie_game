from settings import *
import pygame

# text_map = ['0000000000000',
#             '0101011101010',
#             '0100011100010',
#             '0110001000110',
#             '0111100011110',
#             '0000000000000',
#             '1101101011011',
#             '0000000000000',
#             '0110111110110',
#             '0010001000100',
#             '0010000000100',
#             '0000011100000',
#             '1000010100001']

text_map = ['wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
            'w......................................w',
            'w......................................w',
            'w...wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww...w',
            'w...w..............................w...w',
            'w...w..................................w',
            'w...w.........wwwwwww........w.........w',
            'w...w....w....w.....wwwwww...wwwwwww...w',
            'w...w....w....w........................w',
            'w...w.........w........................w',
            'w.............w.....wwwwwwwwwwwwwww....w',
            'w.............w.....w.............w....w',
            'w...wwwwwwwwwwwwwwwww.............w....w',
            'w......................................w',
            'w......................................w',
            'w...wwwww...wwwwww....wwwwww...wwwwww..w',
            'w...w.......w....w.........w...w....w..w',
            'w...w.......w....w.........w...w....w..w',
            'w...w.......w....w.........w...........w',
            'w...wwwwwwwww....wwwwwwwwwww...........w',
            'w......................................w',
            'w......................................w',
            'w......................................w',
            'w...wwww..wwwwwww..wwwwwwwwwwwwww..wwwww',
            'w...w........w.........w...............w',
            'w...w........w.........w...............w',
            'w...w........w.........w...............w',
            'w...w........wwwwwwwwwww...............w',
            'w......................w...............w',
            'w......................w...............w',
            'w...wwwwwwwwwwwwwwwwwwwwwwwwwww........w',
            'w...w.............w...........w....wwwww',
            'w...w..............................w...w',
            'w...w..............................w...w',
            'w...w.............w................w...w',
            'w...wwwwwwww...wwwwwwwwwwwwwwwwwwwww...w',
            'w......................................w',
            'w......................................w',
            'w......................................w',
            'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
           ]

collision_walls = []
world_map = set()
grid = []
grid_map_new = []
for j, row in enumerate(text_map):
    grid_row = []
    new_grid_row = []
    for i, char in enumerate(row):
        if char == 'w':
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            world_map.add((i * TILE, j * TILE))
            grid_row.append(1)
            for h in range(TILE//zombie_speed):
                new_grid_row.append(1)
        else:
            grid_row.append(0)
            for h in range(TILE//zombie_speed):
                new_grid_row.append(0)
    grid.append(grid_row)
    for i in range(TILE//zombie_speed):
        grid_map_new.append(new_grid_row)
# for i in grid_map_new:
#     print(i)
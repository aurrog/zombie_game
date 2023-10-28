from settings import *
from collections import deque
import map


def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows and not grid[y][x] else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]


def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return queue, visited


grid = map.grid
graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

start = (0, 0)
goal = start
queue = deque([start])
visited = {start: None}


def character_movement(enemy, player):
    player_pos_square = player.pos_square
    start = enemy.pos_square
    queue, visited = bfs(start, player_pos_square, graph)
    goal = player_pos_square
    path_head, path_segment = goal, goal
    path_history = []
    while path_segment and path_segment in visited:
        # pygame.draw.rect(screen, pygame.Color('white'), get_rect(*path_segment), TILE, border_radius=TILE)
        path_history.append([*path_segment])
        path_segment = visited[path_segment]
    step = path_history[len(path_history) - 2]
    step = list((step[0] * TILE + TILE / 2, step[1] * TILE + TILE / 2))
    if enemy.x > step[0]:
        enemy.x -= zombie_speed
    if enemy.x < step[0]:
        enemy.x += zombie_speed
    if enemy.y > step[1]:
        enemy.y -= zombie_speed
    if enemy.y < step[1]:
        enemy.y += zombie_speed
    return enemy.x, enemy.y

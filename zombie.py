from settings import*


class Zombie:
    def __init__(self):
        self.speed = zombie_speed
        self.lives = zombie_lives
        self.x, self.y = zombie_start_position
        self.turn = zombie_start_turn

    @property
    def pos(self):
        return self.x, self.y

    @property
    def pos_square(self):
        return self.x // TILE, self.y // TILE




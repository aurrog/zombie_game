from settings import *


class Zombie:
    def __init__(self, x, y):
        self.speed = zombie_speed
        self.lives = zombie_lives
        self.x, self.y = x, y
        self.turn = zombie_start_turn
        self.bite_cooldown = zombie_bite_cooldown

    @property
    def pos(self):
        return self.x, self.y

    @property
    def pos_square(self):
        return self.x // TILE, self.y // TILE

    def check_bite(self, player):
        if abs(player.x - self.x) < bite_radius and abs(
                player.y - self.y) < bite_radius and self.bite_cooldown >= zombie_bite_cooldown:
            self.bite_cooldown = 0
            zombie_attack_sound.play()
            player_wound_sound.play()
            return player.lives - 1
        else:
            return player.lives

    @property
    def is_alive(self):
        return 1 if self.lives > 0 else 0

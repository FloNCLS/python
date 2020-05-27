from Candy import Candy
from Player import Player


class DizzyCandy(Candy):
    def __init__(self, points, position):
        super().__init__(points, position)
        self.name = 'Dizzy Candy'
        self.sign = 'z'

    def effect(self, player: Player):
        player.points += self.points
        player.warp()

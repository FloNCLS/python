from Player import Player
from Item import Item


class Candy(Item):
    def __init__(self, points, position):
        super().__init__('candy', '*', position)
        self.points = points
        if self.points < 0:
            self.name = 'Sour Candy'
            self.sign = 'o'

        elif self.points == 2:
            self.name = 'Lollipop'
            self.sign = 'P'

    def effect(self, player: Player):
        player.points += self.points

from Item import Item
from Player import Player


class Wall(Item):
    def __init__(self, position):
        super().__init__('Wall', '/', position)

    #
    def bring_item(self, player: Player):
        self.effect(player)

    def effect(self, player: Player):
        player.position = player.previous_position

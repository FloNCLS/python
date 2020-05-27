from Player import Player


class Item:
    registered_items = []

    def __init__(self, name, sign, position):
        self.name = name
        self.sign = sign
        self.position = position
        Item.registered_items.append(self)

    def bring_item(self, player: Player):
        Item.registered_items.remove(self)
        self.effect(player)

    def effect(self, player: Player):
        pass

    @staticmethod
    def get_item(position):
        for item in Item.registered_items:
            if item.position == position:
                return item


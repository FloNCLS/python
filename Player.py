import random


class Player:
    keyboard_key = {'z': (-1, 0),
                    'q': (0, -1),
                    's': (1, 0),
                    'd': (0, 1)}

    registered_players = []

    def __init__(self, name, points=0, start=(0, 0)):
        self.name = name
        self.points = points
        self.position = start
        self.previous_position = self.position
        self.is_alive = True
        Player.registered_players.append(self)

    # Déplacement
    def move(self, game):
        key = input("Mouvement (z,q,s,d) : ")
        while key not in Player.keyboard_key.keys():
            if key == 'p':
                game.pause()
            key = input("Mouvement (z,q,s,d) : ")
        self.previous_position = self.position
        move = Player.keyboard_key[key]

        new_y = self.position[0] + move[0]
        new_x = self.position[1] + move[1]

        if new_y < 0:
            new_y = game.board_size - 1
        elif new_y >= game.board_size:
            new_y = 0
        if new_x < 0:
            new_x = game.board_size - 1
        elif new_x >= game.board_size:
            new_x = 0

        self.position = (new_y, new_x)

    # Téléportation
    def warp(self):
        self.position = (random.randint(0, 9), random.randint(0, 9))

    # Affiche le meilleur score
    @staticmethod
    def get_best_score():
        current_max = 0
        for player in Player.registered_players:
            if current_max < player.points:
                current_max = player.points

        champions = []
        for player in Player.registered_players:
            if player.points == current_max:
                champions.append(player.name)

        print('best score :  ', str(current_max), 'by', champions)

        # Enregistre les meilleurs scores dans best_score.txt
        file = open('best_score.txt', 'w')
        file.write('Meilleur(s) joueur(s) : \n')
        for player in champions:
            file.write(player + ' :  ' + str(current_max) + '\n')
        file.close()

import datetime
import random
from Item import Item
from Candy import Candy
from Player import Player
from DizzyCandy import DizzyCandy
from Wall import Wall


class Game:

    def __init__(self, size=10):
        self.board_size = size
        self.end_time = Game.end_time(1, 0)

    # Dessine le plateau
    def draw(self):
        for line in range(self.board_size):
            for col in range(self.board_size):
                position = (line, col)
                player_position = False
                item_position = False

                item = Item.get_item(position)
                if item is not None:
                    item_position = True

                for player in Player.registered_players:
                    if position == player.position:
                        player_position = True

                if player_position:
                    print('O', end=' ')
                elif item_position:
                    print(item.sign, end=' ')

                else:
                    print('.', end=' ')

            print()

    # Fait apparaitre un bonbon
    def pop_candy(self):
        chance = random.randint(0, 2)
        if chance == 1:
            rand = random.randint(0, 10)
            coord = (random.randint(0, self.board_size), random.randint(0, self.board_size))
            if rand == 0 or rand == 1:
                DizzyCandy(random.randint(-1, 3), coord)
                pass
            elif 1 < rand < 5:
                Wall(coord)
            else:
                Candy(random.randint(-1, 3), coord)

    # Regarde s'il y a un bonbon à prendre (et le prend)
    def check_candy(self, player):
        item = Item.get_item(player.position)
        if item is not None:
            item.bring_item(player)

    # menu du jeu
    def set_game(self):
        try:
            player_amount = int(input('nombre de joueur ?  '))
            if player_amount > 5:
                print('Nombre trop important.')
                self.set_game()
            elif player_amount == 0:
                print('Partie impossible sans joueurs !')
                self.set_game()

            for i in range(0, player_amount):
                Player('Player' + str(i + 1))
            self.play()

        except ValueError:
            print('entrez un nombre valide !')
            self.set_game()

    # Joue une partie complète
    def play(self):
        print("--- Début de la partie ---")

        now = datetime.datetime.today()
        while now < self.end_time:
            for player in Player.registered_players:
                print("C'est au tour de", player.name)
                self.draw()

                now = datetime.datetime.today()

                player.move(self)
                self.check_candy(player)

                if random.randint(1, 3) == 1:
                    self.pop_candy()

                self.draw()

            now = datetime.datetime.today()

            print("----- Terminé -----")
        print(Player.get_best_score())

    # Mise en pause
    def pause(self):
        print('----- Jeu en pause -----')
        begin_time = datetime.datetime.now()

        input('appuyez sur une touche pour reprendre le jeu')
        ending_time = datetime.datetime.now()
        delta_time = ending_time - begin_time
        self.end_time += delta_time
        print('----- Pause terminée -----')

    # retourne le moment où le jeu est censé être fini
    @staticmethod
    def end_time(delta_minute, delta_second):
        delta = datetime.timedelta(minutes=delta_minute, seconds=delta_second)
        end = datetime.datetime.today() + delta
        return end

from tictactoe.game_mechanic import CreateGame
from tictactoe.cpu_ai import Difficulty

class TicTacToe:
    def __init__(
        self,
        difficulty: Difficulty = Difficulty['Medium'],
    ) -> None:

        self.player_input = ''
        self.difficulty = difficulty


    def start_game(self,
                   game: CreateGame = CreateGame
                   ):
        self.game = game().play()
        while self.player_input == '':

            while self.player_input not in ['c', 'q']:
                self.player_input = input('''
                Would you like to play an other game ?
                Press "c" to continue, press "q" to exit the game.
                ''')

            if self.player_input == 'c':
                self.player_input = ''
                self.game = game().play()



if __name__ == '__main__':
    game = TicTacToe().start_game()

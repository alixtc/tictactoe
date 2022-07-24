from tictactoe.game_mechanic import CreateGame

class TicTacToe:
    def __init__(self,
                 game: CreateGame = CreateGame) -> None:
        self.player_input = ''
        self.difficulty = ''
        self.game = game()

    def continue_game(self):
        while self.player_input == '':

            while self.player_input not in ['c', 'q']:
                self.player_input = input('''
                Would you like to play an other game ?
                Press "c" to continue, press "q" to exit the game.
                ''')

            if self.player_input == 'c':
                self.player_input = ''
                self.game = CreateGame().play()


# create game
# plays
# game ends
# ask to continue
# Exit or recreate a new game

if __name__ == '__main__':
    game = TicTacToe().continue_game()

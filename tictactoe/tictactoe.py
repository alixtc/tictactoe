from tictactoe.game_mechanic import CreateGame
from tictactoe.cpu_ai import Difficulty

CONTINUE_MESSAGE = """
Would you like to play an other game ?
Press "c" to continue
Press "q" to exit the game.
Press "d" to change the difficulty"
"""

CHOOSE_DIFFICULTY_MESSAGE = """
Please type desired difficulty level among:
1 - Easy,
2 - Medium,
3 - Hard.
"""

class TicTacToe:
    def __init__(
        self,
        difficulty: Difficulty = Difficulty["Medium"],
    ) -> None:

        self.player_input = ""
        self.difficulty = difficulty

    def start_game(self, game_class = CreateGame) -> None:
        self.game = game_class(self.difficulty).play()
        while self.player_input == "":

            while self.player_input not in ["c", "d", "q"]:
                self.player_input = self.get_player_input()

            if self.player_input == "q":
                return

            if self.player_input == 'd':
                self.difficulty = set_difficulty()


            self.player_input = ""
            self.game = game_class(self.difficulty).play()

    def get_player_input(self) -> str:
        return input(CONTINUE_MESSAGE)

def  set_difficulty() -> Difficulty:
        level  = ''
        while not level:
            user_input = input(CHOOSE_DIFFICULTY_MESSAGE)

            # Set difficulty with full Enum name
            try:
                level = Difficulty[user_input]
            except KeyError:
                pass

            # Set difficulty with Enum number
            try:
               user_input = int(user_input)
               level = Difficulty(user_input)
            except ValueError:
                pass

        return level


if __name__ == "__main__":
    game = TicTacToe().start_game()

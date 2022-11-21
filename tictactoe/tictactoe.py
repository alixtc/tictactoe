from typing import Type

from tictactoe.cpu_ai import Difficulty
from tictactoe.game_mechanic import CreateGame

CONTINUE_MESSAGE = """
Would you like to play an other game ?
Press "c" to continue
Press "q" to exit the game.
Press "d" to change the difficulty"
"""


class TicTacToe:
    def __init__(
        self,
        difficulty: Difficulty = Difficulty["Medium"],
    ) -> None:

        self.player_input = ""
        self.difficulty = difficulty
        self.game = None

    def start_game(self, game_class: Type[CreateGame] = CreateGame) -> None:
        self.game = game_class(self.difficulty).play()
        while self.player_input == "":

            while self.player_input not in ["c", "d", "q"]:
                self.player_input = self.get_player_input()

            if self.player_input == "q":
                return

            if self.player_input == "d":
                self.difficulty = Difficulty.set_difficulty()

            self.player_input = ""
            self.game = game_class(self.difficulty).play()

    def get_player_input(self) -> str:
        return input(CONTINUE_MESSAGE)


if __name__ == "__main__":
    TicTacToe().start_game()

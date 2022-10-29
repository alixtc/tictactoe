from tictactoe.game_mechanic import CreateGame
from tictactoe.cpu_ai import Difficulty


class TicTacToe:
    def __init__(
        self,
        difficulty: Difficulty = Difficulty["Medium"],
    ) -> None:

        self.player_input = ""
        self.difficulty = difficulty

    def start_game(self, game: CreateGame = CreateGame()) -> None:
        self.game = game.play()
        while self.player_input == "":

            while self.player_input not in ["c", "q"]:
                self.player_input = self.get_player_input()

            if self.player_input == "q":
                return

            self.player_input = ""
            self.game = game.play()

    def get_player_input(self) -> str:
        return input(
            """
            Would you like to play an other game ?
            Press "c" to continue, press "q" to exit the game.
            """
        )

def  set_difficulty(level='') -> Difficulty:

        return Difficulty[level]


if __name__ == "__main__":
    game = TicTacToe().start_game()

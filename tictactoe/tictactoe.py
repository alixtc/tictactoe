from tictactoe.game_mechanic import CreateGame
from tictactoe.cpu_ai import Difficulty


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
        return input(
            """
            Would you like to play an other game ?
            Press "c" to continue
            Press "q" to exit the game.
            Press "d" to change the difficulty"
            """
        )

def  set_difficulty() -> Difficulty:
        level  = ''
        while level not in Difficulty.__members__:
            level = input()
        return Difficulty[level]


if __name__ == "__main__":
    game = TicTacToe().start_game()

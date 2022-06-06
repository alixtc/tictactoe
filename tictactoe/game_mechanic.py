from tictactoe.create_board import Board
from tictactoe.cpu_ai import CpuAI
from tictactoe.game_rules import EvaluateVictory
from enum import Enum


class Difficulty(Enum):
    Easy = 1
    Medium = 2
    Hard = 3


class CreateGame:
    def __init__(self, difficulty="Medium") -> None:
        self.board = Board()
        self.cpu = CpuAI(Difficulty[difficulty].value)

    def make_cpu_play(self) -> None:
        # if difficulty medium or above, plays immediate win positions
        if self.cpu.difficulty > 1:
            win_positions = self.cpu.find_sure_win_positions(self.board, "O")
            if win_positions:
                self.board.select_position_on_board("O", int(win_positions[0]))
                return

        # Attempts to prevent easy opponent win on next turn
        if self.cpu.difficulty > 1:
            defeat_positions = self.cpu.find_sure_win_positions(self.board, "X")
            if defeat_positions:
                self.board.select_position_on_board("O", int(defeat_positions[0]))
                return

        choosed_position = self.cpu.pick_valid_position(self.board)
        self.board.select_position_on_board("O", int(choosed_position))

    def make_turn(self) -> str:
        print(str(self.board))

        pos = self.get_valid_user_input()
        self.board.select_position_on_board("X", int(pos))
        if EvaluateVictory(self.board, "X").evaluate_game():
            return "Player 1 has won the game"
        if not self.board.has_empty_positions():
            return "It's a draw !"

        self.make_cpu_play()
        if EvaluateVictory(self.board, "O").evaluate_game():
            return "CPU has won the game"
        if not self.board.has_empty_positions():
            return "It's a draw !"

        return ""

    def get_valid_user_input(self):
        allowed_positions = self.board.get_list_of_valid_positions()

        pos = input("Please select your move:\n")
        while pos not in allowed_positions:
            pos = input(f"Please select your move in {allowed_positions}:\n")
        return pos

    def play(self) -> bool:
        game_result = ""
        while len(game_result) == 0:
            game_result = self.make_turn()

        print(str(self.board))
        print(game_result)
        return False


if __name__ == "__main__":
    game = CreateGame()
    game.play()

from tictactoe.create_board import Board
from tictactoe.cpu_ai import CpuAI, Difficulty
from tictactoe.game_rules import EvaluateVictory


class CreateGame:
    def __init__(self, difficulty: Difficulty = Difficulty["Medium"]) -> None:
        self.result = ""
        self.board = Board()
        self.cpu = CpuAI(difficulty)

    def make_cpu_play(self) -> None:
        # if difficulty medium or above, plays immediate win positions
        if self.cpu.difficulty.value > 1:
            win_positions = self.cpu.find_sure_win_positions(self.board, "O")
            if win_positions:
                self.board.select_position_on_board("O", int(win_positions[0]))
                return

        # Attempts to prevent easy opponent win on next turn
        if self.cpu.difficulty.value > 2:
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
        print(self.result)
        while len(self.result) == 0:
            self.result = self.make_turn()

        print(str(self.board))
        print(self.result)
        return False


if __name__ == "__main__":
    game = CreateGame()
    game.play()

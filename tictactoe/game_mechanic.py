from tictactoe.cpu_ai import CpuAI, Difficulty
from tictactoe.create_board import Board
from tictactoe.game_rules import EvaluateVictory


class CreateGame:
    def __init__(self, difficulty: Difficulty = Difficulty["Medium"]) -> None:
        self.board = Board()
        self.cpu = CpuAI(difficulty)
        self.score_board = dict(
            player=0,
            cpu=0,
            draw=0,
        )

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
        """
        Ask for valid user input and check for victory,
        then does the same for CPU

        ---
        Returns a string indicating the player that won the round, or if it's a
        draw, returns an empty string if no one won this turn.
        """
        print(str(self.board))

        pos = self.get_valid_user_input()
        self.board.select_position_on_board("X", int(pos))
        if EvaluateVictory(self.board, "X").evaluate_game():
            return "player"
        if not self.board.has_empty_positions():
            return "draw"

        self.make_cpu_play()
        if EvaluateVictory(self.board, "O").evaluate_game():
            return "cpu"
        if not self.board.has_empty_positions():
            return "draw"

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

        self.score_board[game_result] += 1

        print(str(self.board))
        print(game_result)
        return False

    def print_score_board(self) -> str:
        """Display scores in formatted string"""
        score_list = [f"{k.upper()}: {v}" for k, v in self.score_board.items()]
        return " | | ".join(score_list)


if __name__ == "__main__":
    game = CreateGame()
    game.play()

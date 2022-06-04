import numpy as np
from tictactoe.create_board import Board


class EvaluateVictory:
    def __init__(self, board: Board, player_marker: str) -> None:
        self.board = board.board
        self.current_player_marker = player_marker

    def evaluate_game(self) -> bool:
        """
        Returns True if the current player has won the game,
        otherwise returns False
        """
        consecutive_3_markers = [self.current_player_marker] * 3

        for line_to_check in self.board:
            if (line_to_check == consecutive_3_markers).all():
                return True

        for col_to_check in self.board.T:
            if (col_to_check == consecutive_3_markers).all():
                return True

        main_diagonal = self.board.diagonal()
        if (main_diagonal == consecutive_3_markers).all():
            return True

        anti_diagonal = np.fliplr(self.board).diagonal()
        if (anti_diagonal == consecutive_3_markers).all():
            return True

        return False

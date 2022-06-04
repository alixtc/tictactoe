from tictactoe.create_board import Board
from typing import List
import numpy as np


class CpuAI:
    pass

    def get_list_of_valid_positions(self, board: Board) -> List[str]:
        current_board = board.board
        x_coordo, y_coordo = np.where((current_board != "X") & (current_board != "O"))
        return [current_board[x, y] for x, y in zip(x_coordo, y_coordo)]

    def pick_valid_position(self, board: Board) -> List[str]:
        positions_list = self.get_list_of_valid_positions(board)
        choice = np.random.choice(positions_list, 1)
        return choice

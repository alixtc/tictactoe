from tictactoe.create_board import Board
from typing import List
import numpy as np
from itertools import chain


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

    def find_sure_win_position(self, board: Board) -> List[str]:
        """
        Go through lines, columns and diags,
        Find all immediate winning positions and returns them in a list
        """

        sequences_to_check = chain(
            [line_to_check for line_to_check in board.board],
            [col_to_check for col_to_check in board.board.T],
            # Diagonal and anti-diagonal
            [board.board.diagonal(), np.fliplr(board.board).diagonal()],
        )
        winning_positions = []

        for seq in sequences_to_check:
            # Make sure that the output is not empty before append
            if win_pos := self.get_immediate_winning_position(seq):
                winning_positions.append(win_pos)

        return winning_positions

    def get_immediate_winning_position(self, sequence: list) -> str:
        """
        Returns string of winning position if immediate win possible
        else returns an empty strin
        g"""
        # Remove current player markers
        if "X" in sequence:
            return ""
        unoccupied_positions = set(sequence).difference("O")
        return list(unoccupied_positions)[0] if len(unoccupied_positions) == 1 else ""

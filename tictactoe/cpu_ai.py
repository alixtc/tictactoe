from tictactoe.create_board import Board
from typing import List
import numpy as np
from itertools import chain
from enum import Enum


class Difficulty(Enum):
    Easy = 1
    Medium = 2
    Hard = 3


class CpuAI:
    def __init__(self, difficulty: Difficulty = Difficulty.Medium):
        self.difficulty = difficulty

    def pick_valid_position(self, board: Board) -> str:
        positions_list = board.get_list_of_valid_positions()
        choice = np.random.choice(positions_list, 1)
        return choice[0]

    def find_sure_win_positions(self, board: Board, marker: str) -> List[str]:
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
            if win_pos := self.identify_win_position_in_sequence(seq, marker):
                winning_positions.append(win_pos)

        return winning_positions

    def identify_win_position_in_sequence(self, sequence: list, marker: str) -> str:
        """
        Returns string of winning position if immediate win possible
        else returns an empty string
        """
        # Remove current player markers
        other_marker = "X" if marker == "O" else "O"
        if other_marker in sequence:
            return ""
        unoccupied_positions = set(sequence).difference(marker)
        return list(unoccupied_positions)[0] if len(unoccupied_positions) == 1 else ""

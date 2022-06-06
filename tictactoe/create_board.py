import numpy as np
from typing import List


class PositionError(Exception):
    pass


class Board:
    def __init__(self) -> None:
        self.board = np.array(range(1, 10), dtype=str).reshape(3, 3)

    def get_list_of_valid_positions(
        self,
    ) -> List[str]:
        """Returns a list with string positions as displayed on the grid"""
        x_coordo, y_coordo = np.where((self.board != "X") & (self.board != "O"))
        return [self.board[x, y] for x, y in zip(x_coordo, y_coordo)]

    def select_position_on_board(self, marker, position: int) -> None:
        if not isinstance(position, int):
            raise PositionError("Please select a valid position")
        if str(position) not in self.board.flatten():
            raise PositionError("Please select a valid position")

        x, y = np.where(self.board == str(position))
        self.board[x, y] = marker

    def has_empty_positions(self):
        empty_positions = [
            item for item in self.board.flatten() if item not in ["X", "O"]
        ]
        return True if len(empty_positions) > 0 else False

    def __str__(self) -> str:
        spacer = "\n" + 9 * "-" + "\n"
        board_string = spacer.join(
            " | ".join(item for item in line) for line in self.board
        )
        return f"\n{board_string}\n"

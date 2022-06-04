import numpy as np


class PositionError(Exception):
    pass


class Board:
    def __init__(self) -> None:
        self.board = np.array(range(1, 10), dtype=str).reshape(3, 3)

    def select_position_on_board(self, marker, position: int) -> None:
        if not isinstance(position, int):
            raise PositionError("Please select a valid position")
        if str(position) not in self.board.flatten():
            raise PositionError("Please select a valid position")

        x, y = np.where(self.board == str(position))
        self.board[x, y] = marker

    def __str__(self) -> str:
        spacer = "\n" + 9 * "-" + "\n"
        board_string = spacer.join(
            " | ".join(item for item in line) for line in self.board
        )
        return f"\n{board_string}\n"

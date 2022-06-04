from tictactoe.create_board import Board
from tictactoe.cpu_ai import CpuAI
import numpy as np


def test_cpu_gets_all_valid_positions():
    board = Board()
    board.board = np.array(
        [["X", "2", "X"], ["4", "O", "6"], ["7", "O", "9"]], dtype=str
    )
    cpu = CpuAI()
    moves = cpu.get_list_of_valid_positions(board)
    assert moves == ["2", "4", "6", "7", "9"]


def test_cpu_pick_valid_position():
    board = Board()
    board.board = np.array(
        [["X", "2", "X"], ["4", "O", "6"], ["7", "O", "9"]], dtype=str
    )
    cpu = CpuAI()

    move = cpu.pick_valid_position(board)
    assert move in cpu.get_list_of_valid_positions(board)

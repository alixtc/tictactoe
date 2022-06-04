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


def test_cpu_find_sure_win_positions():
    board = Board()
    board.board = np.array(
        [["X", "2", "X"], ["4", "O", "6"], ["7", "O", "9"]], dtype=str
    )
    cpu = CpuAI()
    move = cpu.find_sure_win_position(board)
    assert move == ["2"]


def test_cpu_find_sure_win_positions_with_2_positions():
    board = Board()
    board.board = np.array(
        [["X", "O", "X"], ["O", "O", "6"], ["X", "8", "9"]], dtype=str
    )
    cpu = CpuAI()
    assert cpu.find_sure_win_position(board) == ["6", "8"]


def test_get_immediate_winning_position_has_no_win_position():
    cpu = CpuAI()
    sequence = ["O", "4", "X"]
    assert cpu.get_immediate_winning_position(sequence) == ""

    sequence = ["O", "4", "7"]
    assert cpu.get_immediate_winning_position(sequence) == ""


def test_get_immediate_winning_position_has_no_win_position():
    cpu = CpuAI()
    sequence = ["O", "O", "4"]
    assert cpu.get_immediate_winning_position(sequence) == "4"

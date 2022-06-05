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
    move = cpu.find_sure_win_positions(board, "O")
    assert move == ["2"]


def test_cpu_find_sure_win_positions_can_switch_markers():
    board = Board()
    board.board = np.array(
        [["X", "X", "3"], ["4", "O", "6"], ["7", "O", "9"]], dtype=str
    )
    cpu = CpuAI()
    move = cpu.find_sure_win_positions(board, "X")
    assert move == ["3"]


def test_cpu_find_sure_win_positions_with_2_positions():
    board = Board()
    board.board = np.array(
        [["X", "O", "X"], ["O", "O", "6"], ["X", "8", "9"]], dtype=str
    )
    cpu = CpuAI()
    assert cpu.find_sure_win_positions(board, "O") == ["6", "8"]


def test_identify_win_position_in_sequence_has_no_win_position():
    cpu = CpuAI()
    sequence = ["O", "4", "X"]
    assert cpu.identify_win_position_in_sequence(sequence, "O") == ""

    sequence = ["O", "4", "7"]
    assert cpu.identify_win_position_in_sequence(sequence, "O") == ""


def test_identify_win_position_in_sequence_has_win_position():
    cpu = CpuAI()
    sequence = ["O", "O", "4"]
    assert cpu.identify_win_position_in_sequence(sequence, "O") == "4"


def test_identify_win_position_in_sequence_has_win_position():
    cpu = CpuAI()
    sequence = ["X", "X", "4"]
    assert cpu.identify_win_position_in_sequence(sequence, "X") == "4"

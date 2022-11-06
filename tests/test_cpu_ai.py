from unittest.mock import MagicMock, patch
import builtins

import numpy as np
from pytest import MonkeyPatch

from tictactoe.cpu_ai import CpuAI, Difficulty
from tictactoe.create_board import Board


def test_cpu_pick_valid_position():
    board = Board()
    board.board = np.array(
        [["X", "2", "X"], ["4", "O", "6"], ["7", "O", "9"]], dtype=str
    )
    cpu = CpuAI()

    move = cpu.pick_valid_position(board)
    assert move in board.get_list_of_valid_positions()
    assert isinstance(move, str)


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


def test_identify_win_position_in_sequence_has_win_position_with_another_marker():
    cpu = CpuAI()
    sequence = ["X", "X", "4"]
    assert cpu.identify_win_position_in_sequence(sequence, "X") == "4"


@patch("tictactoe.cpu_ai.input", side_effect=["Easy", "Hard"])
def test_set_difficulty_return_appropriate_difficulty(mock_input):
    difficulty = Difficulty.set_difficulty()
    assert difficulty == Difficulty.Easy
    difficulty = Difficulty.set_difficulty()
    assert difficulty == Difficulty.Hard


@patch("tictactoe.cpu_ai.input", side_effect=[1, 133, 3])
def test_set_difficulty_return_difficulty_with_numbers(mock_input: MagicMock):
    difficulty = Difficulty.set_difficulty()
    assert difficulty == Difficulty.Easy
    difficulty = Difficulty.set_difficulty()
    assert difficulty == Difficulty.Hard

    assert mock_input.call_count == 3


# @patch('tictactoe.cpu_ai.input', side_effect= ["Eays", 'Mediume', "Hard"])
def test_set_difficulty_loops_until_appropriate_input(monkeypatch: MonkeyPatch):
    ANSWERS = iter(["Eays", "Mediume", "Hard"])
    monkeypatch.setattr(builtins, "input", value=lambda _: next(ANSWERS))
    difficulty = Difficulty.set_difficulty()
    assert difficulty == Difficulty.Hard

from tictactoe.create_board import Board, PositionError
import numpy as np
import pytest


def test_board_has_9_elements():
    board = Board()
    assert board.board.shape == (3, 3)


def test_add_marker_on_board():
    board = Board()
    board.select_position_on_board("X", 1)
    assert board.board[0, 0] == "X"

    board.select_position_on_board("O", 9)
    assert board.board[2, 2] == "O"


@pytest.fixture
def board():
    board = Board()
    board.board = np.array(
        [["X", "2", "3"], ["4", "5", "6"], ["7", "8", "O"]], dtype=str
    )
    return board


def test_select_position_on_board(board):

    board.select_position_on_board("X", 3)
    assert board.board[0, 2] == "X"
    board.select_position_on_board("X", 5)
    assert board.board[1, 1] == "X"


def test_select_position_on_board_gives_error_if_already_taken(board):
    with pytest.raises(PositionError):
        board.select_position_on_board("X", 0)


def test_select_position_on_board_gives_error_if_position_is_not_int(board):
    with pytest.raises(PositionError):
        board.select_position_on_board("X", "X")


def test_print_board(board):

    board_string = str(board)
    assert "\n" in board_string
    assert " | " in board_string
    assert "-" in board_string

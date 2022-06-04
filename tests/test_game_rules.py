from tictactoe.game_rules import EvaluateVictory
from tictactoe.create_board import Board
import numpy as np


def test_simple_board_has_no_winner():
    board = Board()
    board.board = np.array(
        [["X", "2", "X"], ["4", "O", "6"], ["7", "O", "9"]], dtype=str
    )
    assert EvaluateVictory(board, "X").evaluate_game() == False


def test_simple_board_has_a_line_winner():
    board = Board()
    board.board = np.array(
        [["X", "X", "X"], ["4", "O", "6"], ["7", "O", "9"]], dtype=str
    )
    assert EvaluateVictory(board, "X").evaluate_game() == True


def test_board_has_a_column_winner():
    board = Board()
    board.board = np.array(
        [["X", "X", "X"], ["4", "O", "6"], ["7", "O", "9"]], dtype=str
    ).T
    assert EvaluateVictory(board, "X").evaluate_game() == True


def test_board_has_a_diagonal_winner():
    board = Board()
    board.board = np.array(
        [["X", "2", "O"], ["4", "X", "6"], ["7", "O", "X"]], dtype=str
    )
    assert EvaluateVictory(board, "X").evaluate_game() == True


def test_board_has_an_anti_diagonal_winner():
    board = Board()
    board.board = np.array(
        [["1", "O", "X"], ["4", "X", "6"], ["X", "O", "9"]], dtype=str
    )
    assert EvaluateVictory(board, "X").evaluate_game() == True


def test_player_2_has_won_the_game():
    board = Board()
    board.board = np.array(
        [["X", "O", "X"], ["4", "O", "6"], ["X", "O", "9"]], dtype=str
    )
    assert EvaluateVictory(board, "O").evaluate_game() == True

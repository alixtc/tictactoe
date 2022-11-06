from tictactoe.game_mechanic import CreateGame
from tictactoe.create_board import Board
from tictactoe.cpu_ai import CpuAI, Difficulty
import tictactoe.game_mechanic as gm

import numpy as np


def test_create_game_generate_a_board_and_cpu():
    game = CreateGame()
    assert isinstance(game.board, Board)
    assert isinstance(game.cpu, CpuAI)


def test_make_cpu_play():
    game = CreateGame()

    original_positions = game.board.get_list_of_valid_positions()
    game.make_cpu_play()
    final_position = game.board.get_list_of_valid_positions()

    assert len(final_position) == len(original_positions) - 1


def test_make_cpu_play_prevents_easy_win_if_difficulty_equals_hard():
    game = CreateGame(Difficulty.Hard)
    game.board.board = np.array(
        [["1", "X", "X"], ["4", "O", "6"], ["O", "8", "9"]], dtype=str
    )
    game.make_cpu_play()
    assert game.board.board[0, 0] == "O"


def test_make_cpu_play_win_easy_grid_if_difficulty_atleast_medium():
    game = CreateGame()
    game.board.board = np.array(
        [["X", "X", "O"], ["4", "O", "6"], ["7", "8", "9"]], dtype=str
    )
    game.make_cpu_play()
    assert game.board.board[2, 0] == "O"


def test_make_turn():
    game = CreateGame()

    def mock_input(message: str):
        return "1"

    gm.input = mock_input

    game.make_turn()
    assert game.board.board[0, 0] == "X"
    assert "O" in game.board.board
    assert game.board.has_empty_positions() == True


def test_make_turn_has_user_win_the_game():
    game = CreateGame()
    game.board.board = np.array(
        [["1", "X", "X"], ["4", "O", "6"], ["7", "O", "9"]], dtype=str
    )

    def mock_input(messages: str):
        return "1"

    gm.input = mock_input

    final_turn = game.make_turn()
    assert final_turn == "Player 1 has won the game"


def test_make_turn_has_no_winner():
    game = CreateGame()
    game.board.board = np.array(
        [["X", "O", "X"], ["O", "X", "O"], ["O", "8", "9"]], dtype=str
    )

    def mock_input(messages: str):
        return "8"

    gm.input = mock_input
    assert game.make_turn() == "It's a draw !"


def test_play_has_cpu_win_the_game():
    game = CreateGame()
    game.board.board = np.array(
        [["O", "X", "X"], ["O", "5", "O"], ["7", "8", "O"]], dtype=str
    )

    def mock_input(messages: str):
        return "8"

    gm.input = mock_input

    assert game.play() == False


## TODO add test for bad position entered, ask again to enter position


def test_make_turn_wait_for_valid_position_input_from_player():
    game = CreateGame()
    game.board.board = np.array(
        [["1", "X", "X"], ["4", "O", "6"], ["O", "8", "9"]], dtype=str
    )

    # Mock 2 consecutives values for input(), first one invalid, second valid
    answers = iter(["2", "5", "4"])

    def mock_input(messages: str):
        return answers.__next__()

    gm.input = mock_input

    game.make_turn()

    # first 2 values are unchanged
    assert game.board.board[0, 1] == "X"
    assert game.board.board[1, 1] == "O"
    assert game.board.board[1, 0] == "X"


def test_play_can_be_interrupted_using_game_result():
    game = CreateGame()
    game.result = "Stop"
    assert game.play() == False

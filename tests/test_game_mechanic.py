from unittest.mock import MagicMock, patch

import numpy as np

import tictactoe.game_mechanic as gm
from tictactoe.cpu_ai import CpuAI, Difficulty
from tictactoe.create_board import Board
from tictactoe.game_mechanic import CreateGame


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

    turn_message = game.make_turn()
    assert "player" in turn_message


def test_make_turn_has_no_winner():
    game = CreateGame()
    game.board.board = np.array(
        [["X", "O", "X"], ["O", "X", "O"], ["O", "8", "9"]], dtype=str
    )

    def mock_input(messages: str):
        return "8"

    gm.input = mock_input
    assert "draw" in game.make_turn()


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


def test_CreateGame_has_score_board_attribute():
    game = CreateGame()
    assert hasattr(game, "score_board")


@patch.object(CreateGame, "make_turn", side_effect=["draw", "player", "cpu"])
def test_score_board_adds_one_to_counter_when_player_wins(mock_turn: MagicMock):
    game = CreateGame()

    game.play()
    assert game.score_board["draw"] == 1
    assert mock_turn.call_count == 1


@patch.object(
    CreateGame,
    "make_turn",
    side_effect=["draw", "draw", "player", "player", "cpu", "cpu", "player"],
)
def test_score_board_adds_multiple_consecutive_wins(mock_turn: MagicMock):
    game = CreateGame()
    for _ in range(7):
        game.play()

    assert game.score_board["draw"] == 2
    assert game.score_board["player"] == 3
    assert game.score_board["cpu"] == 2
    assert mock_turn.call_count == 7


def test_print_score_board_has_3_components():
    game = CreateGame()
    score = game.print_score_board()
    assert "draw".upper() in score
    assert "cpu".upper() in score
    assert "player".upper() in score

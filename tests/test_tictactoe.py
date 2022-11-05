import builtins
from unittest.mock import MagicMock, patch

from pytest import MonkeyPatch

from tictactoe.cpu_ai import Difficulty
from tictactoe.game_mechanic import CreateGame
from tictactoe.tictactoe import TicTacToe, set_difficulty


def mock_play():
    pass


@patch.object(CreateGame, "play")
@patch("tictactoe.tictactoe.input")
def test_tictactoe_exits_when_player_enters_q(
    mock_input: MagicMock, mock_game_play: MagicMock
):
    mock_input.side_effect = "q"

    party = TicTacToe()
    party = party.start_game()

    assert party == None
    mock_input.assert_called_once()
    mock_game_play.assert_called_once()


@patch("tictactoe.game_mechanic.CreateGame.play", side_effect=mock_play)
@patch("tictactoe.tictactoe.input", side_effect=["e", "q"])
def test_tictactoe_aks_again_when_player_input_not_valid(mock_input, mock_play):
    party = TicTacToe()
    party = party.start_game()

    assert party == None
    mock_input.assert_called()


@patch("tictactoe.game_mechanic.CreateGame.play", side_effect=mock_play)
@patch("tictactoe.tictactoe.input", side_effect=["c", "q"])
def test_TTT_creates_a_new_game_when_asked_to_continue(mock_input, mock_play):
    party = TicTacToe()
    party.start_game()
    assert not hasattr(party.game, "board")


def test_TTC_has_a_difficulty_setting():
    party = TicTacToe()
    assert isinstance(party.difficulty, Difficulty)


@patch("tictactoe.tictactoe.input", side_effect=["Easy", "Hard"])
def test_set_difficulty_return_appropriate_difficulty(mock_input):
    difficulty = set_difficulty()
    assert difficulty == Difficulty.Easy
    difficulty = set_difficulty()
    assert difficulty == Difficulty.Hard

@patch("tictactoe.tictactoe.input", side_effect=[1, 133, 3])
def test_set_difficulty_return_difficulty_with_numbers(mock_input: MagicMock):
    difficulty = set_difficulty()
    assert difficulty == Difficulty.Easy
    difficulty = set_difficulty()
    assert difficulty == Difficulty.Hard

    assert mock_input.call_count == 3


# @patch('tictactoe.tictactoe.input', side_effect= ["Eays", 'Mediume', "Hard"])
def test_set_difficulty_loops_until_appropriate_input(monkeypatch: MonkeyPatch):
    ANSWERS = iter(["Eays", "Mediume", "Hard"])
    monkeypatch.setattr(builtins, "input", value=lambda _: next(ANSWERS))
    difficulty = set_difficulty()
    assert difficulty == Difficulty.Hard


@patch("tictactoe.tictactoe.set_difficulty", return_value=Difficulty.Hard)
@patch("tictactoe.game_mechanic.CreateGame.play", side_effect=mock_play)
@patch("tictactoe.tictactoe.input", side_effect=["d", "q"])
def test_TTT_can_change_difficulty_after_game(
    mock_input: MagicMock, mock_play: MagicMock, mock_difficulty: MagicMock
):
    party = TicTacToe()
    assert party.difficulty == Difficulty.Medium
    party.start_game()
    assert party.difficulty == Difficulty.Hard

    # Final check sequence
    assert mock_play.call_count == 2
    assert mock_input.call_count == 2
    mock_difficulty.assert_called_once()

from tictactoe.cpu_ai import Difficulty
from tictactoe.tictactoe import TicTacToe, set_difficulty
from unittest import mock

def mock_play():
    pass

@mock.patch('tictactoe.game_mechanic.CreateGame.play', side_effect=mock_play)
@mock.patch('tictactoe.tictactoe.input', side_effect='q')
def test_tictactoe_exits_when_player_enters_q(mock_input, mock_play):
    party = TicTacToe()
    party = party.start_game()

    assert party == None
    mock_input.assert_called_once()
    mock_play.assert_called_once()

@mock.patch('tictactoe.game_mechanic.CreateGame.play', side_effect=mock_play)
@mock.patch('tictactoe.tictactoe.input', side_effect= ["e", "q"])
def test_tictactoe_aks_again_when_player_input_not_valid(mock_input, mock_play):
    party = TicTacToe()
    party = party.start_game()

    assert party == None
    mock_input.assert_called()

@mock.patch('tictactoe.game_mechanic.CreateGame.play', side_effect=mock_play)
@mock.patch('tictactoe.tictactoe.input', side_effect= ["c", "q"])
def test_TTT_creates_a_new_game_when_asked_to_continue(mock_input, mock_play):
    party = TicTacToe()
    party.start_game()
    assert not hasattr(party.game, "board")


def test_TTC_has_a_difficulty_setting():
    party = TicTacToe()
    assert isinstance(party.difficulty, Difficulty)


@mock.patch('tictactoe.tictactoe.input', side_effect= ["Easy", "Hard"])
def test_set_difficulty_return_appropriate_difficulty(mock_input):
    difficulty = set_difficulty()
    assert difficulty == Difficulty.Easy
    difficulty = set_difficulty()
    assert difficulty == Difficulty.Hard


@mock.patch('tictactoe.tictactoe.input', side_effect= ["Eays", 'Mediume', "Hard"])
def test_set_difficulty_loops_until_appropriate_input(mock_input):
    difficulty = set_difficulty()
    assert difficulty == Difficulty.Hard


@mock.patch('tictactoe.game_mechanic.CreateGame.play', side_effect=mock_play)
@mock.patch('tictactoe.tictactoe.input', side_effect= ["d", "q"])
@mock.patch('tictactoe.tictactoe.set_difficulty', return_value=Difficulty.Hard)
def test_TTT_can_change_difficulty_after_game(mock_input,
                                              mock_play,
                                              mock_difficulty):
    party = TicTacToe()
    assert party.difficulty == Difficulty.Medium
    party.start_game()
    assert party.difficulty == Difficulty.Hard

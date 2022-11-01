from tictactoe.cpu_ai import Difficulty
from tictactoe.game_mechanic import CreateGame
from tictactoe.tictactoe import TicTacToe, set_difficulty
from unittest import mock



class MockCreateGame(CreateGame):
    def play(self):
        pass

@mock.patch('tictactoe.tictactoe.input', side_effect='q')
def test_tictactoe_exits_when_player_enters_q(mock_input):
    party = TicTacToe()
    party = party.start_game(MockCreateGame())

    assert party == None
    mock_input.assert_called_once()


@mock.patch('tictactoe.tictactoe.input', side_effect= ["e", "q"])
def test_tictactoe_aks_again_when_player_input_not_valid(mock_input):
    party = TicTacToe()
    party = party.start_game(MockCreateGame())

    assert party == None
    mock_input.assert_called()

@mock.patch('tictactoe.tictactoe.input', side_effect= ["c", "q"])
def test_TTT_creates_a_new_game_when_asked_to_continue(mock_input):
    party = TicTacToe()
    party.start_game(MockCreateGame())
    assert not hasattr(party.game, "board")


def test_TTC_has_a_difficulty_setting():
    party = TicTacToe()
    assert isinstance(party.difficulty, Difficulty)


def test_set_difficulty_return_difficulty():
    difficulty = set_difficulty('Easy')
    assert difficulty == Difficulty['Easy']


def test_set_difficulty_can_be_parametrized():
    difficulty = set_difficulty('Hard')
    assert difficulty == Difficulty['Hard']

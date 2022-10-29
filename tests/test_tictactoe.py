from tictactoe.cpu_ai import Difficulty
from tictactoe.game_mechanic import CreateGame
from tictactoe.tictactoe import TicTacToe, set_difficulty


class MockCreateGame(CreateGame):
    def play(self):
        pass


def test_tictactoe_exits_when_player_enters_q():
    party = TicTacToe()

    def mock_input() -> str:
        return "q"

    party.get_player_input = mock_input
    party = party.start_game(MockCreateGame())

    assert party == None


def test_tictactoe_aks_again_when_player_input_not_valid():
    party = TicTacToe()

    ANSWERS = iter(["e", "q"])

    def mock_input() -> str:
        return ANSWERS.__next__()

    party.get_player_input = mock_input
    party = party.start_game(MockCreateGame())

    assert party == None


def test_TTT_creates_a_new_game_when_asked_to_continue():
    party = TicTacToe()

    ANSWERS = iter(["c", "q"])

    def mock_input():
        return ANSWERS.__next__()

    party.get_player_input = mock_input

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

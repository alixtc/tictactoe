from tictactoe.create_board import Board
from tictactoe.game_mechanic import CreateGame
from tictactoe.tictactoe import TicTacToe
import tictactoe.tictactoe as ttt

class MockCreateGame:
    def play(self):
        pass

def test_tictactoe_exits_when_player_enters_q():
    party = TicTacToe()

    def mock_input(messages: str):
        return "q"

    ttt.input = mock_input
    party = party.continue_game()

    assert party == None


def test_tictactoe_aks_again_when_player_input_not_valid():
    party = TicTacToe()

    answers = iter(["e", "q"])

    def mock_input(messages: str):
        return answers.__next__()

    ttt.input = mock_input
    party = party.continue_game()

    assert party == None


def test_TTT_creates_a_new_game_when_asked_to_continue():
    party = TicTacToe()
    party.game.board = []

    answers = iter(["c", "q"])
    def mock_input(messages: str):
        return answers.__next__()
    ttt.input = mock_input

    # Simulate ask to continue
    ttt.CreateGame = MockCreateGame
    party.continue_game()

    # Restore initial state after mocking
    ttt.CreateGame = CreateGame

    assert not hasattr(party.game, 'board')



def test_TTC_creates_a_new_game():
    party = TicTacToe()
    assert isinstance(party.game, CreateGame)

from game_of_greed.game import Game
from tests.flow.flo import Flo


def test_quitter():
    Flo.test('tests/flow/quitter.sim.txt')
    
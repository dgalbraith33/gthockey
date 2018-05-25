from django.test import TestCase
from .models import Game, Team


class GameTestCase(TestCase):

    def test_game_opponent_name(self):
        game = Game(date='2018-01-01', time='00:01', opponent=Team(school_name='test'))
        self.assertEquals(game.opponent_name(), "test")

    def test_game_opponent_name_none(self):
        game = Game(date='2018-01-01', time='00:01')
        self.assertIsNone(game.opponent_name())

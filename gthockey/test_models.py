from django.test import TestCase
from datetime import datetime, date, time

from .models import Game, Team, Rink


class GameTestCase(TestCase):

    def test_game_datetime(self):
        game = Game(date=date(2018, 1, 1), time=time(2, 30))
        self.assertEquals(game.datetime, datetime(2018, 1, 1, 2, 30))

    def test_game_datetime_no_time(self):
        game = Game(date=date(2018, 1, 1))
        self.assertEquals(game.datetime, datetime(2018, 1, 1,))

    def test_game_time_fmt(self):
        game = Game(time=time(11, 15))
        self.assertEquals(game.get_time(), "11:15 AM")

    def test_game_time_fmt_strip(self):
        game = Game(time=time(13, 15))
        self.assertEquals(game.get_time(), "1:15 PM")

    def test_game_time_fmt_none(self):
        game = Game()
        self.assertEquals(game.get_time(), "TBD")

    def test_game_opponent_name(self):
        game = Game(opponent=Team(school_name='test'))
        self.assertEquals(game.opponent_name(), "test")

    def test_game_opponent_name_none(self):
        game = Game()
        self.assertIsNone(game.opponent_name())

    def test_game_rink_name(self):
        game = Game(location=Rink(rink_name='test_rink'))
        self.assertEquals(game.rink_name(), "test_rink")

    def test_game_rink_name_none(self):
        game = Game()
        self.assertEquals(game.rink_name(), "TBD")

    def test_game_is_reported(self):
        game = Game(score_gt_final=10, score_opp_final=0)
        self.assertTrue(game.is_reported)

    def test_game_gt_not_reported(self):
        game = Game(score_opp_final=0)
        self.assertFalse(game.is_reported)

    def test_game_opp_not_reported(self):
        game = Game(score_gt_final=10)
        self.assertFalse(game.is_reported)

    def test_game_upcoming(self):
        game = Game(date=date(2100, 1, 1))
        self.assertEquals(game.get_result(), "Upcoming")
        self.assertEquals(game.short_result, "U")

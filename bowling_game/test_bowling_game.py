import unittest
from bowling_game import Game


class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.number_of_plays = 20

    def test_if_game_and_score_exists(self):
        pins = 0
        score = self._roll_many(self.number_of_plays, pins)
        self.assertEqual(0, score)

    def test_counting_score(self):
        pins = 1
        score = self._roll_many(self.number_of_plays, pins)
        self.assertEqual(20, score)

    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self._roll_many(17, 0)
        self.assertEqual(16, self.game.score())

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self._roll_many(16, 0)
        self.assertEqual(24, self.game.score())

    def _roll_many(self, number_of_plays, pins):
        for play in range(self.number_of_plays):
            self.game.roll(pins)
        return self.game.score()

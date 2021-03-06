"""Tests for mind controllers and other wizards."""

import axelrod

from .test_player import TestPlayer

C, D = axelrod.Action.C, axelrod.Action.D


class TestMindController(TestPlayer):

    name = "Mind Controller"
    player = axelrod.MindController
    expected_classifier = {
        "memory_depth": -10,
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": True,  # Finds out what opponent will do
        "manipulates_state": False,
    }

    def test_strategy(self):
        """ Will always make opponent cooperate """

        p1 = axelrod.MindController()
        p2 = axelrod.Cooperator()
        self.assertEqual(p1.strategy(p2), D)
        self.assertEqual(p2.strategy(p1), C)

    def test_vs_defect(self):
        """ Will force even defector to cooperate """

        p1 = axelrod.MindController()
        p2 = axelrod.Defector()
        self.assertEqual(p1.strategy(p2), D)
        self.assertEqual(p2.strategy(p1), C)

    def test_vs_grudger(self):
        """ Will force even Grudger to forget its grudges"""

        p1 = axelrod.MindController()
        p2 = axelrod.Grudger()
        for _ in range(4):
            p1.history.append(D, C)
            p2.history.append(C, D)
        self.assertEqual(p1.strategy(p2), D)
        self.assertEqual(p2.strategy(p1), C)


class TestMindWarper(TestMindController):

    name = "Mind Warper"
    player = axelrod.MindWarper
    expected_classifier = {
        "memory_depth": -10,
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": True,  # Finds out what opponent will do
        "manipulates_state": False,
    }

    def test_setattr(self):
        player = self.player()
        player.strategy = lambda opponent: C

    def test_strategy(self):
        player = self.player()
        opponent = axelrod.Defector()
        play1 = player.strategy(opponent)
        play2 = opponent.strategy(player)
        self.assertEqual(play1, D)
        self.assertEqual(play2, C)


class TestMindBender(TestMindController):

    name = "Mind Bender"
    player = axelrod.MindBender
    expected_classifier = {
        "memory_depth": -10,
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": True,  # Finds out what opponent will do
        "manipulates_state": False,
    }

    def test_strategy(self):
        player = self.player()
        opponent = axelrod.Defector()
        play1 = player.strategy(opponent)
        play2 = opponent.strategy(player)
        self.assertEqual(play1, D)
        self.assertEqual(play2, C)

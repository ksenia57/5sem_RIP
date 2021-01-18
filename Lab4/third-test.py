import unittest
from unittest import TestCase
from third import Context
from third import Upakovka, Dostavka, Sborka


class ThirdTestOne(TestCase):

    def setUp(self):
        self.Context = Context()

    def firstTest(self):
        context = Context(Upakovka())
        self.assertEqual("Началась упаковка...\nУпаковка кончилась, перехожу к доставке", context.upakovka())

    def secTest(self):
        context = Context(Dostavka())
        self.assertEqual("ОТКАЗАНО => Ещё не доставлено - сборка невозможна", context.sborka())


class ThirdTestTwo(TestCase):
    def firstTest(self):
        context = Context(Dostavka())
        self.assertEqual("ОТКАЗАНО => Ещё не доставлено - сборка невозможна", context.sborka())


if __name__ == "__main__":
    unittest.main()

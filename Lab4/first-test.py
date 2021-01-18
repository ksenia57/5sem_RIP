import unittest
from unittest import TestCase
from unittest.mock import patch
from first import TableFactory
from first import ChairFactory
from third import Context
from third import Upakovka, Dostavka, Sborka


class factoryTestCase(TestCase):
#   def start(self):
#        factory = TableFactory()

    @patch('first.define_mat', return_value="дерево")
    def test_mat(self, define_mat):
        factory = TableFactory()
        material = factory.create_material()
        self.assertEqual("Создание стола из материала дерево", material.paint(define_mat("platform")))

    @patch('first.define_mat', return_value="металл")
    def test_mat(self, define_mat):
        factory = ChairFactory()
        material = factory.create_material()
        self.assertEqual("Создание стула из материала металл", material.paint(define_mat("platform")))

    @patch('first.define_stil', return_value="современном")
    def test_mat(self, define_stil):
        factory = TableFactory()
        style = factory.create_style()
        self.assertEqual("В современном стиле", style.paint(define_stil("stilchik")))

    @patch('first.define_stil', return_value="классическом")
    def test_mat(self, define_stil):
        factory = ChairFactory()
        style = factory.create_style()
        self.assertEqual("В классическом стиле", style.paint(define_stil("stilchik")))


class ThirdTestOne(TestCase):

#    def setUp(self):
#       self.Context = Context()

    def firstTest(self):
        context = Context(Upakovka())
        self.assertEqual("Началась упаковка...\nУпаковка кончилась, перехожу к доставке", context.upakovka())

    def secTest(self):
        context = Context(Dostavka())
        self.assertEqual("ОТКАЗАНО => Ещё не доставлено - сборка невозможна", context.sborka())


if __name__ == '__main__':
    unittest.main()

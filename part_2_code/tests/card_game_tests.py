import unittest
from src.card import Card
from src.card_game import CardGame



class TestCardGame(unittest.TestCase):

    def setUp(self):

        self.card1 = Card("hearts", 1)
        self.card2 = Card("spades", 8)
        self.card3 = Card("diamonds", 11)
        self.game1 = CardGame()
        self.cards = [self.card1, self.card2, self.card3]


    def test_check_for_ace(self):
        self.game1.check_for_ace(self.card1)
        self.assertEqual(self.card1.value, 1)

    def test_highest_card(self):
        self.game1.highest_card(self.card2, self.card3)
        self.assertGreater(self.card3.value, self.card2.value)

    def test_cards_total(self):
        self.game1.cards_total(self.cards)
        message = self.game1.cards_total(self.cards)
        self.assertEqual("You have a total of 20" , message)

import unittest

from set_check import set_check

class SetCheckTest(unittest.TestCase):
    def test_empty_card_list(self):
        filename = "test_data/empty_card_list.csv"
        with open(filename) as f:
            cards_list = f.read().splitlines()
        results = set_check(cards_list)
        expected = {
            'setExistance': False,
            'setList': []
        }
        self.assertEqual(expected, results)
    def test_two_cards(self):
        filename = "test_data/fewer_than_three_cards.csv"
        with open(filename) as f:
            cards_list = f.read().splitlines()
        results = set_check(cards_list)
        expected = {
            'setExistance': False,
            'setList': []
        }
        self.assertEqual(expected, results)

    def test_no_sets_in_cards(self):
        filename = "test_data/no_set_in_cards.csv"
        with open(filename) as f:
            cards_list = f.read().splitlines()
        results = set_check(cards_list)
        expected = {
            'setExistance': False,
            'setList': []
        }
        self.assertEqual(expected, results)

    def test_one_set_in_cards(self):
        filename = "test_data/one_set_in_cards.csv"
        with open(filename) as f:
            cards_list = f.read().splitlines()
        results = set_check(cards_list)
        expected = {
            'setExistance': True,
            'setList': [['gd1e', 'gd1l', 'gd1s']]
            }
        self.assertEqual(expected, results)

    def test_multiple_sets_in_cards(self):
        filename = "test_data/multiple_sets_in_cards.csv"
        with open(filename) as f:
            cards_list = f.read().splitlines()
        results = set_check(cards_list)
        expected = {
            'setExistance': True,
            'setList': [['gd3s', 'ps2e', 'ro1l'],
                        ['go1l', 'ro3e', 'po2s'],
                        ['go1e', 'ro3l', 'po2s'],
                        ['ro1l', 'ro2l', 'ro3l']]
        }
        self.assertEqual(expected, results)

    # TODO add in test to check for all same, all diff, combo sets
    # TODO check behavior for multiple of the same card

if __name__ == '__main__':
    unittest.main()

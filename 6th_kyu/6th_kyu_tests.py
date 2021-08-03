import unittest

from autocomplete_yay import autocomplete
from break_camelCase import remove_camelCase
from unique_in_order import unique_in_order

class Test_Autocomplete(unittest.TestCase):

    def test_filtering(self):
        dictionary = ['abnormal', 'Arm-wrestling', 'absolute', 'airplane', 'airport', 'amazing','apple', 'ball']
        self.assertEqual(autocomplete('ai', dictionary), ['airplane','airport'])

    def test_no_more_than_5(self):
        dictionary = ['ab', 'ac', 'ad', 'ae', 'af', 'ag']
        self.assertEqual(autocomplete('a', dictionary), ['ab', 'ac', 'ad', 'ae', 'af'])

    def test_no_matches(self):
        dictionary = ['c1', 'c2',]
        self.assertEqual(autocomplete('b', dictionary), [])

    def test_keep_same_order(self):
        dictionary = ['ag', 'af', 'ae', 'ad']
        self.assertEqual(autocomplete('a', dictionary), ['ag', 'af', 'ae', 'ad'])

    def test_no_non_alpha_input(self):
        dictionary = ['c1', 'c2',]
        self.assertEqual(autocomplete('!c', dictionary), ['c1', 'c2'])

class Test_RemoveCamelCase(unittest.TestCase):

    def test_normal_camelCase(self):
        self.assertEqual(remove_camelCase('wordWord'), 'word Word')

    def test_ignore_initial_capital(self):
        self.assertEqual(remove_camelCase('WordWord'), 'Word Word')

    def test_ignore_if_preceeding_space(self):
        self.assertEqual(remove_camelCase('word Word'), 'word Word')

class Test_UniqueInOrder(unittest.TestCase):

    def test_ints(self):
        self.assertEqual(unique_in_order([1, 3, 3, 3, 2, 2, 1, 3]), [1, 3, 2, 1, 3])

    def test_strings(self):
        self.assertEqual(unique_in_order(['pen', 'car', 'pen', 'pen', 'lion', 'boat', 'boat', 'boat', 'boat', 'cup']), ['pen', 'car', 'pen', 'lion', 'boat', 'cup'])

    def test_strings_and_ints(self): 
        self.assertEqual(unique_in_order(['pen', 1, 1, 'car', 'car', 'car', 3567, 3567, 'pen', 'car']), ['pen', 1, 'car', 3567, 'pen', 'car'])

    def test_empty_list(self):
        self.assertEqual(unique_in_order([]), [])

    def test_single_item(self):
        self.assertEqual(unique_in_order(['single']), ['single'])

    def test_double_item(self):
        self.assertEqual(unique_in_order([2,2]), [2])


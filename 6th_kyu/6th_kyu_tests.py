import unittest

from autocomplete_yay import autocomplete
from break_camelCase import remove_camelCase

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

    # tests:
    # wordWord - basic
    # WordWord - with first cap
    # Word Word - already a space
    pass







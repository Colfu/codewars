import unittest

from autocomplete_yay import autocomplete

class TestAutocomplete(unittest.TestCase):

    

    def test_remove_occurrences(self):
        dictionary = ['abnormal', 'Arm-wrestling', 'absolute', 'airplane', 'airport', 'amazing','apple', 'ball']

        self.assertEqual(autocomplete('ai', dictionary), ['airplane','airport'])
        self.assertEqual(autocomplete('-a', dictionary), ['abnormal','Arm-wrestling','absolute','airplane','airport'])










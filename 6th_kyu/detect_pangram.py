# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once
# (case is irrelevant).   **Cr.4
#
# Given a string, detect whether or not it is a pangram. **Cr.1
# Return True if it is, False if not. **Cr.2
# Ignore numbers and punctuation. **Cr.3
# -------------------------

import unittest

def is_pangram(sentence):
    """
    Check if input is a pangram or not.

    A pangram is a sentence that contains every single letter of the alphabet at least once.
    Ignores numbers and punctuation.

    :param sentence: string
    :return: True / False
    """
    # store alphabet to compare sentences to        **Cr.3
    pangram_check_string = 'abcdefghijklmnopqrstuvwxyz'

    # convert all characters to lowercase for ease of comparison  **Cr.4
    sentence = sentence.casefold()

    # compare alphabet string to sentence one letter at a time   **Cr.1 & 2
    for letter in pangram_check_string:
        if letter not in sentence:
            return False
        else:
            continue
    return True



class TestIsPangram(unittest.TestCase):

    def test_correct_pangram(self):
        self.assertEqual(is_pangram("the quick, brown fox jumps over the lazy dog"), True)

    def test_incorrect_pangram(self):
        self.assertEqual(is_pangram("The quick, brown fox jumps over the sleepy dog!"), False)

    def test_ignore_nums(self):
        self.assertEqual(is_pangram("The 6 quick, brown foxes jump over 20 lazy dogs!"), True)

    def test_ignore_punctuation(self):
        self.assertEqual(is_pangram("The quick! brown fox? jumps over the lazy dogs!"), True)

    def test_ignore_case(self):
        self.assertEqual(is_pangram("THE quick BROWN fox JUMPS over THE lazy DOG"), True)

    def test_not_enough_letters(self):
        self.assertEqual(is_pangram("The brown fox jumps"), False)


if __name__ == '__main__':
    unittest.main()

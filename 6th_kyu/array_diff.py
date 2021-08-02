# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
#
# It should remove all values from list a,
# which are present in list b keeping their order.      **Cr.1
# array_diff([1,2],[1]) == [2]

# If a value is present in b,
# all of its occurrences must be removed from the other:        **Cr.2
# array_diff([1,2,2,2,3],[2]) == [1,3]
# ---------
# Plan:
# for each item in list a, if not in list b, add to list c

import unittest


def array_diff(all_values_list, unneeded_values_list):
    """
    Subtract values of 2nd list from the 1st list

    :param all_values_list: list
    :param unneeded_values_list: list
    :return: results_list
    """

    # store the needed results
    results_list = []

    # If value from 1st list is not in 2nd list, add to 3rd list
    for letter in all_values_list:
        if letter in unneeded_values_list:
            pass
        else:
            results_list.append(letter)
    return results_list


class TestArrayDiff(unittest.TestCase):

    def test_remove_occurrences(self):
        self.assertEqual(array_diff([1, 2], [1]), [2])
        self.assertEqual(array_diff([1, 2, 2, 2, 3, 3, 4, 55, 678], [2, 3, 55]), [1, 4, 678])


# run the unit tests rather than the actual function
if __name__ == '__main__':
    unittest.main()
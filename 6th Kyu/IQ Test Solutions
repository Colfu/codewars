def iq_test(string_of_nums):
    """
    Finds which number is different in evenness from a given list of numbers

    :param: list_of_nums - input is list of ints
    :return: index of 'different' int, using real indexes (starting fom 1 not 0)
    """

    # convert string of numbers into list of ints
    nums_list = list(map(int, string_of_nums.split()))

    # create new list with odd/even instead of numbers, using modulo operator to decide if odd/even
    odd_even_list = []
    for num in nums_list:
        if (num % 2) == 0:
            odd_even_list.append('even')
        else:
            odd_even_list.append('odd')

    # store the 'real' index of the uneven number when found - Cr.1
    uneven_number_real_index = None

    # count the number of times each item is in the list, if it's one then it is the uneven number
    for odd_even in odd_even_list:
        if odd_even_list.count(odd_even) == 1:
            uneven_number_real_index = odd_even

    # return the index of the uneven number, adding 1 to get the 'real' index - Cr.2
    return odd_even_list.index(uneven_number_real_index) +1

print(iq_test("2 4 7 8 10"), 'should be: 3')
print(iq_test("1 2 2"), 'should be: 1')

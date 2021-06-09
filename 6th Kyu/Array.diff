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

def array_diff(a, b):
    c = []              #results list
    for letter in a:
        if letter in b:
            pass
        else:
            c.append(letter)        
    return c


#  best practice answer:
# def array_diff(a, b):
#     return [x for x in a if x not in b]

# Complete the method which returns the number which is most frequent in the given input array. **Cr.1
# If there is a tie for most frequent number, return the largest number among them.         **Cr.2
#
# Note: no empty arrays will be given.
#
# Examples
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
# ------------------
# Plan:
# Use dictionary 'get' method
# look for max value   - Cr.1
#  add keys of max value to list,
# look for val being equal to another - use max - Cr 2

def highest_rank(arr):
    nums_dict = {}              # dictionary to count nums into
    for num in arr:
        nums_dict[num] = nums_dict.get(num, 0) +1           # if num not in dict, add with value 0, else value +1
    # print(nums_dict)

    highest_value = (0, 0)         # place holder for highest num  Cr.1
    for k,v in nums_dict.items():     # searches list of tuples and finds highest value
        if v > highest_value[1]:
            highest_value = (k,v)
    # print(highest_value)

    highest_value_list = []
    for k,v in nums_dict.items():
        if v == highest_value[1]:              # find all the k,v pairs with highest v, and add k to new list
            highest_value_list.append(k)
    # print(highest_value_list)

    return max(highest_value_list)      #Cr.2

# soneone else's (simpler?) soultion

# def highest_rank(arr):
#     best = 0
#     occs = 0
#     for item in arr:
#         times = arr.count(item)
#         if times > occs:
#             best = item
#             occs = times
#         elif times == occs:
#             if best < item:
#                 best = item
#     return best

# It's time to create an autocomplete function! Yay!
# The autocomplete function will take in an input string and a dictionary array
# and return the values from the dictionary that start with the input string. **Cr.1
# If there are more than 5 matches, restrict your output to the first 5 results.   **Cr.2
# If there are no matches, return an empty array.                               **Cr.3
#
# Example:
# autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']
#
# For this kata, the dictionary will always be a valid array of strings.
# Please return all results in the order given in the dictionary,       **Cr.4
# even if they're not always alphabetical.
# The search should NOT be case sensitive, but the case of the word should be preserved when it's returned.  **Cr.5
# For example, "Apple" and "airport" would both return for an input of 'a'.
# However, they should return as "Apple" and "airport" in their original cases. **Cr.6
#
# Important note:
# Any input that is NOT a letter should be treated as if it is not there.   **Cr.7
# For example, an input of "$%^" should be treated as "" and an input of "ab*&1cd" should be treated as "abcd".
# -----------------------------------
# Plan:
# Assumption: they say 'dictionary' but mean 'list', as that's what they show in the example.
# 1. for word in dictionary, if word[0:len of input] = input, add to results list
# 2. case sensitive using .lower()
# 3. filter using >= a and <=z



def autocomplete(input_, dictionary):
    """Take in an input string and a dictionary array and return 
    the values from the dictionary that start with the input string.

    Args:
        input_ (string): letters used to start a word
        dictionary (list): valid list of strings

    Returns:
        list: values from dictonary list that start with input_ string
    """
    # Make lowercase, remove non-alpha characters, and store   **Cr.7
    filtered_input = ''
    for char in input_.lower():       
        if char >= 'a' and char <= 'z':     
            filtered_input += char          

    # Store results
    autocomplete_list = []          
    for word in dictionary:
        # Compare characters in length of input to same length of each dictionary word, if the same, add to results list
        if word[:(len(filtered_input))].lower() == filtered_input.lower():      #**Cr.5 & 6
            autocomplete_list.append(word)          #  **Cr.1, **Cr.4
    # If no matches, return empty list
    if len(autocomplete_list) == 0:         # **Cr.3
        return []
    else:
        return autocomplete_list[:5]        # **Cr.2

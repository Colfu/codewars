# Complete the solution so that the function will break up camel casing,
# using a space between words.
#
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
# -----------------------------------------
# Plan:
# loop through string, add to new string
# if case is cap, add with a preceding space
# unsure whether it includes upper camel case as well, so sort out 1st letter in case

def solution(camelCase_string):
    """ Break up camel casing, using a space between words.

    Args:
        camelCase_sting ([string]): Some words using camelCase

    Returns:
        new_string [string]: String with camelCase removed
    """
    # start new string with index 0 so the following does not try to add space
    new_string = camelCase_string[0]               
    
    # Ignore 1st letter incase of cap, add each letter to new string, and if Capital then add preceeding space
    for x in camelCase_string[1:]:                 
        if x.islower():
            new_string += x         
        else:
            new_string += ' ' + x       
    return new_string


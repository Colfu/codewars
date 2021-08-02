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

def solution(s):
    new_string = s[0]               # start new string with index 0 so the following does not try to add space
    for x in s[1:]:                 # everything except the first letter in case it's a cap
        if x.islower():
            new_string += x         # add to new string
        else:
            new_string += ' ' + x       # add with preceding space
    return new_string


# print(solution("HelloWorld"), "should be: Hello World")


def remove_camelCase(camelCase_string):
    """ Break up camel casing, using a space between words.

    Example:
    "camelCasing"  =>  "camel Casing"
    "identifier"   =>  "identifier"

    Args:
        camelCase_sting [string]: Some words using camelCase
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


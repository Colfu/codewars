# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def duplicate_count(text):
    text = text.lower()     #Cr.1
    char_dict = {}
    dupl_char_dict = []
    for char in text:
        char_dict[char] = char_dict.get(char,0) +1
#    print(char_dict)
    for k,v in char_dict.items():
        if v > 1:           #Cr.2
            dupl_char_dict.append(k)
#            print(dupl_char_dict)
    return(len(dupl_char_dict))

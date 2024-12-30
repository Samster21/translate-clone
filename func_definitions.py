import string

def identify(strng:str):
    strng = list(strng)

    #If given a range of characters
    if len(strng) == 3 and strng[1] == "-":
        return [chr(i) for i in range (ord(strng[0]), ord(strng[2])+1)]
    
    #If given uppercase
    if strng == "[:upper:]":
        return list(string.ascii_uppercase)
    
    #If given lowercase
    if strng == "[:lower:]":
        return list(string.ascii_lowercase)
    
    #For other than this case
    return [strng[i] for i in range(len(strng))]

def translate(user_input:str,set1:str, set2:str):

    user_input = list(user_input)

    range_1 = identify(set1)
    range_2 = identify(set2)

    for i in range(len(user_input)):

        #See if the current element is in the first range. For example, if the (from) range is [A-Z], then the 'x' in "Axe" should not be translated.
        if user_input[i] in range_1:

            #Find the position of the current character in the range. For example, the 'b' in Bob lies in index 1 of [a-z]
            position = range_1.index(user_input[i])

            try:
                user_input[i] = range_2[position]
            
            #Edge case where the second set is smaller than the first, prevents index error
            except IndexError:
                user_input[i] = range_2[len(range_2)-1]

    return ''.join(user_input)

def delete(user_input:str,set1:str):
    user_input = list(user_input)
    range_1 = identify(set1)
    deleted_text = [char for char in user_input if char not in range_1]
    return ''.join(deleted_text)
   




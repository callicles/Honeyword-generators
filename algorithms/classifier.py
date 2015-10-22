from constants import ENGLISH_INDEX

def isInAlphabeticalSequence(word):
    """
    Checks if the string passed to it is in an alphabetical sequence
    """
    if len(word) == 1:
        return False
    else:
        for i in range(len(word) - 1):
            if ord(word[i]) != ord(word[i + 1]) + 1:
                return False
        return True

def isInReverseAlphabeticalSequence(word):
    """
    Checks if the string passed to it is in a reverse alphabetical sequence
    """
    if len(word) == 1:
        return False
    else:
        for i in range(len(word) - 1):
            if ord(word[i]) != ord(word[i + 1]) - 1:
                return False
        return True

def isSameCharacterSequence(word):
    """
    Checks if the string passed to it is in a sequence of identical characters
    """
    if len(word) == 1:
        return False
    else:
        for i in range(len(word) - 1):
            if word[i] != word[i + 1]:
                return False
        return True

def isOnlySpecialCharacters(word):
    """
    Checks if the string passed is comprised entirely of special characters typically allowed in passwords
    """
    for i in range(len(word)):
        if word[i].isalpha() or word[i].isdigit():
            return False
    return True

def isInSequence(word):
    """
    Checks if the string passed is a sequence of digits logically connected ("e.g. 369")
    """
    if len(word)<3:
        return False
    else:
        increment = int(word[0]) - int(word[1])
        for i in range(len(word) - 2):
            if int(word[i+1]) - int(word[i+2]) != increment:
                return False
        return True

def classifyCharacter(word):
    """
    Classifies the passed single character string into an alphabet, number, or special character
    """
    if word[0].isalpha():
        return "isalpha"
    elif word[0].isalpha():
        return "isdigit"
    else:
        return "isspecialchar"

def classifier(token):

    """ Classifies the given token into one of several categories.
    categories currently defined are:
        same_sequence_letters: same letter being repeated (e.g. "aaa")
        sequence_letters: letters in alphabetical sequence or reverse alphabetical sequence (e.g. "abc", "zyx")
        random_letters: string of random letters (e.g. dyumd)
        same_sequence_numbers: same digit being repeated (e.g. "22222")
        sequence_numbers: logical sequence of digits (e.g. "369")
        even_numbers: all digits are even digits (e.g. "4824")
        odd_numbers: all digits are odd digits (e.g. "35573")


    Classifies by priority:
    words: constant sequence > sequence > random
    numbers: constant sequence > sequence > odd or even > random numbers
    special chars: constant sequence > random
    """

    #check if token is a string of alphabets


    if token.isalpha():
        #check if token is a sequence of the same alphabet:
        if isSameCharacterSequence(token):
            return "same_sequence_letters"
        elif isInAlphabeticalSequence(token) or isInReverseAlphabeticalSequence(token):
            return "sequence_letters"
        else:
            return "random_letters"

    #check if token is a number
    elif token.isdigit():
        if isSameCharacterSequence(token):
            return "same_sequence_numbers"
        elif isInSequence(token):
            return "sequence_numbers"
        else:
            evenCount = 0
            oddCount = 0
            for x in range(len(token)):
                if int(token[x])%2 ==0:
                    evenCount+=1
                else:
                    oddCount+=1
            if evenCount == len(token):
                return "even_numbers"
            elif oddCount == len(token):
                return "odd_numbers"
            else:
                return "random_numbers"
    else:
        if isSameCharacterSequence(token):
            return "same_sequence_specialchars"
        else:
            return "random_specialchars"



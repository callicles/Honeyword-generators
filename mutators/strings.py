import string
from random import shuffle, randint, choice
import editdistance

from algorithms.constants import LEET_MAPPER


def mutate_random(word, length=-1):
    """ Mutates a random string randomly
    :param word: string to be mutated
    :param length: length of the desired output, if left blank output will be the same.
    :return: new string
    """
    new_string = ""

    if length == -1:
        length = len(word)

    for i in range(0, len(word)):
        if (randint(0, 1)) == 1:
            new_string += choice(string.printable)
        else:
            new_string += word[i]

    if length < len(word):
        new_string = new_string[length:]
    elif length > len(word):
        for i in range(length - len(word)):
            new_string += choice(string.printable)

    return new_string


def mutate_sequence(word):
    """ Mutates a string sequence like "abcde" into another string sequence
    :param word: string with a sequence
    :return: another string with a different sequence
    """
    if len(word) < 25:
        start_index = randint(0, 26 - len(word))
    else:
        start_index = randint(0, 25)

    new_sequence = ""
    for i in range(len(word)):
        new_sequence += string.ascii_lowercase[(start_index + i) % 26]

    return new_sequence


def change_syntactic_word(word, database):
    """ Change the word in a syntactic manner
    :param word: word to be changed
    :return: other word that is syntactically close to the first one
    """

    min = 999999
    words = []

    for line in database:  #englishWords.txt"):
        ed = editdistance.eval(line,word)
        if(ed < min and ed != 0):
            min = ed

    for line in database:
        ed = editdistance.eval(line,word)
        if(ed - min  < 3 and ed - min > - 3 ):
            words.append(line)

    #print words

    shuffle(words)

    return words[0]


def mutate_leet_speak(word):
    """ change some letters in the string to be in leet speak
    :param word: string to be mutated
    :return: Leet speak string
    """
    if len(word) < 2:
        return word

    # We only want to change maximum half of the word
    number_of_changes = randint(1, len(word) / 2)
    written_changes = 0
    new_string = ""

    for c in word:
        if randint(0, 1) == 1 and written_changes < number_of_changes:
            if len(LEET_MAPPER[c][0]) == 1:
                new_string += LEET_MAPPER[c][0]
                written_changes += 1
            else:
                new_string += c
        else:
            new_string += c

    return new_string


def mutate_caps(word):
    """ Change caps in the string
    :param word: string to change caps
    :return: mutated string
    """
    if len(word) < 2:
        return word

    # We only want to change maximum half of the word
    number_of_changes = randint(1, len(word) / 2)
    written_changes = 0
    new_string = ""

    for c in word:
        if randint(0, 1) == 1 and written_changes < number_of_changes:
            new_string += c.upper()
        else:
            new_string += c

    return new_string


def mutate_constant(word):
    """ changes a sequence of constant string "aaaa" in another constant
    string
    :param word: String to be changed
    :return: constant string of the same length
    """
    char = string.ascii_letters[randint(0, 51)]
    new_sequence = ""
    for i in range(0, len(word)):
        new_sequence += char

    return new_sequence

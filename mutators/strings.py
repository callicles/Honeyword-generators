import nltk
from textblob import Word
from random import shuffle, randint, choice

__author__ = 'nicolas'
nltk.download('wordnet')


def change_word(word):
    """ Get another word close to the requested word to replace it
    :param word: Word to replace
    :return: new word
    """
    word = Word(word)
    words = []

    for synset in word.synsets[:]:
        for synonym in synset.lemma_names():
            words.append(synonym.replace('_', ''))
        for hyponym in synset.hyponyms():
            for lemma in hyponym.lemma_names():
                words.append(lemma.replace('_', ''))
    shuffle(words)

    return words[:1]


def mutate_random(string, length=-1):
    """ Mutates a random string randomly
    :param string: string to be mutated
    :param length: length of the desired output, if left blank output will be the same.
    :return: new string
    """
    new_string = string

    if length == -1:
        length = len(string)

    for i in range(randint(1, len(string))):
        if (randint(0, 1)) == 1:
            new_string[i] = choice(string.printable)

    if length < len(string):
        new_string = new_string[length:]
    elif length > len(string):
        for i in range(length - len(string)):
            new_string += choice(string.printable)

    return new_string


def mutate_sequence(string):
    """ Mutates a string sequence like "abcde" into another string sequence
    :param string: string with a sequence
    :return: another string with a different sequence
    """


def mutate_special_chars(special_chars):
    """ Change some special chars into other
    :param special_chars:
    :return:
    """

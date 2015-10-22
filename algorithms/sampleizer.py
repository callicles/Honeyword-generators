from random import randint, shuffle
import editdistance


def sample(database, index, n):
    """
    Get all sample from the database
    :param database: Rock you password database
    :param index: index of the given password
    :param n: length of the sample size
    :return: list of passwords
    """
    l = [database[randint(0, index)]]

    if n > 2:
        for i in range(0, n-2):
            l.append(database[randint(0, len(database))])

    return l


def get_similar_passwords(password, database):
    """ Get another word close to the requested word to replace it
    :param word: Word to replace
    :return: new word
    """
    min = 999999
    words = []
    for line in database:  # englishWords.txt"):
        ed = editdistance.eval(line, password)

        if ed < min and ed != 0:
            min = ed

    for line in database:
        ed = editdistance.eval(line,password)
        if ed - min  < 2 and ed - min > - 2:
            words.append(line)

    # print words
    shuffle(words)
    return words

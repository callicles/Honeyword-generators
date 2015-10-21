import random
import string

__author__ = 'nicolas'


def mutate_sequence(number_sequence):
    """ Mutates a number sequence into another number sequence
    :param number_sequence: String representing a sequence
    :return: String representing a different sequence
    """
    sequence_padding = int(number_sequence[1]) - int(number_sequence[0])
    new_sequence = "" + str(random.randint(0, 9))

    for i in range(len(number_sequence)):
        new_sequence += str(int(new_sequence[i]) + sequence_padding)

    return new_sequence


def mutate_random(random_numbers):
    """ Mutates a batch of random numbers into different random numbers
    :param random_numbers: String representing random numbers
    :return: String representing other random numbers
    """
    new_numbers = ""
    for i in range(len(random_numbers)):
        new_numbers += str(random.randint(0, 9))

    return new_numbers


def mutate_all_odds(odd_numbers):
    """ Mutates a string of odds numbers in an other string of odd numbers
    :param odd_numbers: String of odd numbers
    :return: string of other odd numbers
    """
    new_numbers = ""
    for i in range(len(odd_numbers)):
        new_numbers += str(random.choice(range(1, 9, 2)))

    return new_numbers


def mutate_all_even(even_numbers):
    """ Mutates a string of even numbers in an other string of even numbers
    :param even_numbers: string of even numbers
    :return: string of other even numbers
    """
    new_numbers = ""
    for i in range(len(even_numbers)):
        new_numbers += str(random.choice(range(0, 9, 2)))

    return new_numbers


def mutate_constant(numbers):
    """ changes a sequence of constant string "1111" in another constant
    string
    :param numbers: String to be changed
    :return: constant string of the same length
    """
    char = string.digits[random.randint(0, 9)]
    new_sequence = ""
    for i in range(0, len(numbers)):
        new_sequence += char

    return new_sequence

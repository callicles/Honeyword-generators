import mutators.numbers
import mutators.strings
import random
import collections

def generateHoneyWord(password, database):
    for token in password['tokens']:
        if(token == 'words'):
            for word in password['tokens'][token]:
                apply_word_mutation(word, database)
        if(token == 'sequence_letters'):
            for string_sequence in password['tokens'][token]:
                apply_string_sequence_mutation(string_sequence)
        if(token == 'same_sequence_letters'):
            for string_sequence_same in password['tokens'][token]:
                apply_string_sequence_same_mutation(string_sequence_same)
        if(token == 'random_letters' or token == 'same_sequence_specialchars' or token == 'random_specialchars'):
            for random_string in password['tokens'][token]:
                apply_random_string_mutation(random_string)
        if (token == 'sequence_numbers'):
            for number_sequence in password['tokens'][token]:
                apply_number_sequence_mutation(number_sequence)
        if(token == 'same_sequence_numbers'):
            for number_sequence_same in password['tokens'][token]:
                apply_number_sequence_same_mutation(number_sequence_same)
        if(token == 'random_numbers'):
            for random_number in password['tokens'][token]:
                apply_random_numbers_mutation(random_number)
        if(token == 'odd_numbers'):
            for odd_number in password['tokens'][token]:
                apply_odd_numbers_mutation(odd_number)
        if(token == 'even_numbers'):
            for even_number in password['tokens'][token]:
                apply_even_numbers_mutation(even_number)

    return generateNewPasswordFromMutatedWord(password)

def generateNewPasswordFromMutatedWord(password):
    output_pass = ''
    password_components = {}
    for token in password['tokens']:
        for mutation in password['tokens'][token]:
            password_components[mutation['start_index']] = mutation['content']

    order = collections.OrderedDict(sorted(password_components.items()))

    for index, component in order.iteritems():
        output_pass += component

    return output_pass

def apply_number_sequence_same_mutation(word):
    rnd = random.random()
    if(rnd < 1.0):
        word['content'] = mutators.numbers.mutate_constant(word['content'])

def apply_number_sequence_mutation(word):
    rnd = random.random()
    if(rnd < 1.0):
        word['content'] = mutators.numbers.mutate_sequence(word['content'])

def apply_random_numbers_mutation(word):
    rnd = random.random()
    if(rnd < 1.0):
        word['content'] = mutators.numbers.mutate_random(word['content'])

def apply_odd_numbers_mutation(word):
    rnd = random.random()
    if(rnd < 0.5):
        word['content'] = mutators.numbers.mutate_all_odds(word['content'])

def apply_even_numbers_mutation(word):
    rnd = random.random()
    if(rnd < 1.0):
        word['content'] = mutators.numbers.mutate_all_even(word['content'])

def apply_random_string_mutation(word):
    rnd = random.random()
    if(rnd < 1.0):
        word['content'] = mutators.strings.mutate_random(word['content'])

def apply_string_sequence_mutation(word):
    rnd = random.random()
    if(rnd < 1.0):
        word['content'] = mutators.strings.mutate_sequence(word['content'])

def apply_string_sequence_same_mutation(word):
    rnd = random.random()
    if(rnd < 1.0):
        word['content'] = mutators.strings.mutate_constant(word['content'])


def apply_word_mutation(word, database):
    rnd = random.random()
    if(rnd < 0.5):
        word['content'] = mutators.strings.change_syntactic_word(word['content'], database)
    else:
        word['content'] = word['content']

    rnd = random.random()
    if(rnd < 0.99):
         word['content'] = mutators.strings.mutate_caps(word['content'])
    if(rnd >= 0.99):
        word['content'] = mutators.strings.mutate_leet_speak(word['content'])
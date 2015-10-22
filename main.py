import pprint
import argparse
import mutators
from algorithms.password_leaner import password_leaner
from algorithms.tokeniser import tokeniser
from algorithms import generators

pp = pprint.PrettyPrinter(indent=1)

def main(password):

    nicolasObject = password_leaner(password)
    rishavObject = tokeniser(nicolasObject)

    for i in range(1000):
        markObject = generators.generateHoneyWord(rishavObject)

        #pp.pprint(rishavObject)
        pp.pprint(markObject)

"""
parser = argparse.ArgumentParser(description='Generate honey words from a list '
                                             'of passwords')

parser.add_argument('N',
                    metavar='n',
                    nargs='1',
                    type=int,
                    help='number of sweet words to be generated'
                         ' list')

parser.add_argument('input_passwords_file',
                    metavar='input',
                    nargs='1',
                    help='The file with the passwords to put transform into'
                         ' honey words')

parser.add_argument('output_passwords_file',
                    metavar='input',
                    nargs='1',
                    help='The file with the passwords to put the honey words in'
                         ' list')

args = parser.parse_args()
"""

main("password123")

"""
pp.pprint(password_leaner("!!n0t.@n0th3r.d@mn.p@$$w0rd!!"))
print mutators.numbers.mutate_all_odds("135")
print mutators.numbers.mutate_all_even("028")
print mutators.numbers.mutate_random("2398")
print mutators.numbers.mutate_sequence("2345")

print mutators.strings.mutate_leet_speak("another")
print mutators.strings.mutate_sequence("abc")
print mutators.strings.change_semantic_word("another")
print mutators.strings.mutate_constant("aaaa")
print mutators.strings.mutate_random("lashdkj")
print mutators.strings.mutate_caps("iuywebn")
"""

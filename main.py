import pprint
import argparse
import mutators
import os.path
from algorithms.password_leaner import password_leaner
from algorithms.tokeniser import tokeniser
from algorithms import generators
from random import shuffle

pp = pprint.PrettyPrinter(indent=1)


def justGetPassword(password):

    count = 0
    for i in range(len(password)-1,0,-1):
        if(password[i] != ' '):
            count+=1
        else:
            break

    return password[len(password)-count:len(password)]


def main(password, number):

    honeywords = [password]

    database = []

    if os.path.isfile("resources/rockyou-withcount.txt"):
        database_count = 1

        for line in open("resources/rockyou-withcount.txt"):
            database.append(justGetPassword(line[:-1]))
            database_count += 1
            if database_count > 100000:
                break

    print database[0]
    print len(database)

    for i in range(number):
        nicolasObject = password_leaner(password)
        rishavObject = tokeniser(nicolasObject)
        markObject = generators.generateHoneyWord(rishavObject, database)
        #pp.pprint(rishavObject)
        honeywords.append(markObject.strip())

    shuffle(honeywords)
    print honeywords
    return honeywords


parser = argparse.ArgumentParser(description='Generate honey words from a list '
                                             'of passwords')

parser.add_argument('n', type=int)
parser.add_argument('input_passwords_file', type=file)
parser.add_argument('output_passwords_file', type=argparse.FileType('w+'))

args = parser.parse_args()

for password in args.input_passwords_file:
    for honey in main(password, args.n):
        args.output_passwords_file.write(honey + ",")
    args.output_passwords_file.write("\n")


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

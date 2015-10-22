import pprint
import argparse
import os.path
from algorithms.password_leaner import password_leaner
from algorithms.tokeniser import tokeniser
from algorithms import generators, sampleizer
from random import shuffle, randint

pp = pprint.PrettyPrinter(indent=1)


def justGetPassword(password):

    count = 0
    for i in range(len(password)-1,0,-1):
        if(password[i] != ' '):
            count+=1
        else:
            break

    return password[len(password)-count:len(password)]


def main(password, number, database):

    password = password.strip()

    honeywords = [password]

    try:
        password_index = database.index(password)
    except ValueError:
        password_index = -1

    if password_index != -1:
        honeywords = honeywords + sampleizer.sample(database, password_index, number)
    else:
        if len(database) > 100:
            sample = sampleizer.get_similar_passwords(password, database)
            if len(sample) < number:
                take_number = randint(0, len(sample))
            else:
                take_number = randint(0, number)
            for i in range(0, take_number):
                honeywords.append(sample[i])
            number = number - take_number

        if number > -1:
            for i in range(number-1):
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

database = []

if os.path.isfile("resources/rockyou-withcount.txt"):
    database_count = 1

    for line in open("resources/rockyou-withcount.txt"):
        database.append(justGetPassword(line[:-1]))
        database_count += 1
        if database_count > 100000:
            break

for password in args.input_passwords_file:
    args.output_passwords_file.write(",".join(main(password, args.n, database)) + "\n")

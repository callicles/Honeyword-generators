from constants import MAX_LEET_CHAR, ENGLISH_INDEX, LEET_MAPPER, LEET_REVERSE_MAPPER
import pprint
import mutators.numbers1

pp = pprint.PrettyPrinter(indent=1)


def password_leaner(password):
    """ Returns an understandable password

    This function takes in a password that can be 123pa$$w0rd45 and turns it into 123password45
    The aim is to map l33t speak to real words so that we can work on the meaning instead of its
    written implementation
    """

    # Replacing the characters in the password by their leet equivalent
    linted_pass = ""
    for i in range(0, len(password)):
        found_match = ""
        for j in range(1, MAX_LEET_CHAR):
            if password[i:i+j] in LEET_REVERSE_MAPPER and len(found_match) < len(password[i:i+j]):
                found_match = password[i:i+j]

        if len(found_match) > 0:
            # In Leet speak to Latin char there are only 6 multiple mappings for a character
            # for simplification sake we only consider the first and (for most chars) only one correspondence
            linted_pass = linted_pass + LEET_REVERSE_MAPPER[found_match][0]

        else:
            linted_pass = linted_pass + password[i]

    # Finding the words inside the linted password
    found_words = []
    for word, bool in ENGLISH_INDEX.iteritems():
        index = linted_pass.find(word)
        if index != -1 and len(word) > 0:
            found_words.append({
                "content": word,
                "start_index": index,
                "end_index": index + len(word) - 1
            })

    # Finding the words that are significant in the found words
    found_words = sorted(found_words, key=lambda k: k['start_index'])
    significant_words = [found_words[0]]
    pointer = 0

    for word in found_words:
        if significant_words[pointer]['start_index'] == word['start_index'] and significant_words[pointer]['end_index'] < word['end_index']:
            significant_words[pointer] = word
        elif significant_words[pointer]['end_index'] < word['start_index']:
            pointer += 1
            significant_words.append(word)

    # Putting all the results back together in the easy to read manner.
    output = ""
    pointer = 0
    last_word_end_index = 0
    for i in range(0, len(password)):
        if pointer < len(significant_words) and i == significant_words[pointer]['start_index']:
            last_word_end_index = significant_words[pointer]['end_index']
            output = output + significant_words[pointer]['content']
            pointer += 1
        elif i > last_word_end_index:
            output = output + password[i]

    # Returning the result in an output that can be used
    return {
        "source_pass": password,
        "mapped_pass": output,
        "tokens": {
            "words": significant_words
        }
    }



pp.pprint(password_leaner("!!n0t.@n0th3r.d@mn.p@$$w0rd!!"))
print mutators.numbers1.mutate_all_odds("135")
print mutators.numbers1.mutate_all_even("028")
print mutators.numbers1.mutate_random("2398")
print mutators.numbers1.mutate_sequence("2345")

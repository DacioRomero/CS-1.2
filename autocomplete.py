'''Displays all possible endings of the ending of a provided word'''
import sys
import dictionary_words


def fuzzy_startswith(string, prefix):
    '''Checks if one string starts with another regardless of case.

    Args:
        string: A string whose beginning will be checked.
        prefix: A string that used for checking.

    Returns:
        True if string1 starts with string2 regardlesss of case else False.
    '''
    return string.upper().startswith(prefix.upper())


def autocomplete(part, dictionary):
    '''Creates list of words that finish the provided word.

    Args:
        part: A string representing the beginning of a word.

    Returns:
        A list of the different words that complete word as strings.
    '''
    possibilities = []

    for dict_word in dictionary:
        if fuzzy_startswith(dict_word, part):
            possibilities.append(dict_word)

    return possibilities


def main():
    '''Tests autocomplete().'''
    part = sys.argv[1]
    dictionary = dictionary_words.get_dictionary()
    print('\n'.join(autocomplete(part, dictionary)))


if __name__ == '__main__':
    main()

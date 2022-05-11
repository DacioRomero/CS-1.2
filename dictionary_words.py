'''Displays a random psuedo-sentence.'''
import random
import sys


def get_dictionary():
    '''Creates a list of words.

    Args: None.

    Returns:
        A list of words from the OSX dictionary.
    '''
    # TODO: Read from common dictionary for Windows support
    with open('/usr/share/dict/words') as file:
        raw_file = file.read()

    return raw_file.splitlines()


def create_random_sentence(dictionary, num_words):
    '''Creates a psuedo-sentence.

    Args:
        dictionary: A list of words from which the sentence will
            be constructed.
        num_words: An int of the number of words in the sentence.

    Returns:
        A "sentence" from words in dictionary with num_words
        number of words represented as a string.
    '''
    return ' '.join(random.choice(dictionary) for _ in range(num_words))


def main():
    '''Tests get_dictionary() and create_random_sentence().'''
    print(create_random_sentence(get_dictionary(), num_words=int(sys.argv[1])))


if __name__ == '__main__':
    main()

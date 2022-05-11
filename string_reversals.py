'''Displays the reverse a word or sentence.'''
import sys


def word(the_word):
    '''Reverses a word.

    Args:
        the_word: The string representing a words.

    Returns:
        The variable word reversed.
    '''
    return the_word[::-1]


def sentence(the_sentence):
    '''Reverses a sentence's words.

    Args:
        the_sentence: A string of a sentence.
    Returns:
        A new sentence with the words of the setence reversed.``
    '''
    return ' '.join(the_sentence.split(' ')[::-1])


def main():
    '''Tests word() or sentence().'''
    if sys.argv[1] == 'word':
        print(word(the_word=sys.argv[2]))

    elif sys.argv[1] == 'sentence':
        print(sentence(the_sentence=' '.join(sys.argv[2:])))

if __name__ == '__main__':
    main()

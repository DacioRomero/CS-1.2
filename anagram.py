'''Displays an anagram of a provided word.'''
import sys
import dictionary_words


def generate(word):
    '''Generates one-word anagrams of a word.

    Args:
        word: The word to create anagrams from.

    Returns:
        A list of different anagrams from a word.
    '''
    word_list = []

    for dictionary_word in dictionary_words.get_dictionary():
        if is_anagram(word, dictionary_word):
            word_list.append(dictionary_word)

    return word_list


def is_anagram(word1, word2):
    '''Checks if two words are anagrams of each other.

    Args:
        word1: A word.
        word2: Another word.

    Returns:
        True if word1 and word2 are anagrams of each other else False.
    '''
    word1_up = word1.upper()
    word2_up = word2.upper()

    return word1_up != word2_up and sorted(word1_up) == sorted(word2_up)


def main():
    '''Tests generator().'''
    print(' '.join(generate(word=sys.argv[1])))


if __name__ == '__main__':
    main()

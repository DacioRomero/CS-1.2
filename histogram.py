'''Generates a histogram of the frequency of words in a text.'''
import re

# Matches latin-esque words
WORD_RE = re.compile(r'[a-zA-Z]+(?:\'[a-z]+)?')


def generate_histogram_dict(text):
    '''Generates a histogram of a string.

    Args:
        text: The string to generate from.

    Returns:
        A dictionary of unique words each with a value of their occurences.
    '''
    if isinstance(text, str):
        words = get_words(text)
    else:
        words = text

    histogram = {}

    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram


def generate_histogram_ll(text):
    '''Generates a histogram of a string.

    Args:
        text: The string to generate from.

    Returns:
        A list of lists in the format [[word, occurences], ...].
    '''
    words = get_words(text)
    words.sort()

    histogram = []

    for index, word in enumerate(words):
        if index > 0 and word == words[index - 1]:
            histogram[-1][1] += 1
        else:
            histogram.append([word, 1])

    return histogram


def generate_histogram_lt(text):
    '''Generates a histogram of a string.

    Args:
        text: The string to generate from.

    Returns:
        A list of tuples in the format [(word, occurences), ...].
    '''
    words = get_words(text)
    words.sort()

    histogram = []
    count = 1

    for index, word in enumerate(words):
        if index == 0:
            continue

        word_prev = words[index - 1]

        if word == word_prev:
            count += 1
        else:
            histogram.append((word_prev, count))
            count = 1

    return histogram


def get_words(text):
    '''Gets the words in a text.

    Args:
        text: The string to parse.

    Returns:
        A list of strings of the words in a text.
    '''
    # Find all words using regex, make them lowercase, and put them in a list
    return [word.lower() for word in WORD_RE.findall(text)]


def unique_words(histogram):
    '''Counts the number of unique words in a histogram.

    Args:
        histogram: The histogram (dictonary) to check.

    Returns:
        The number of unique words in the histogram.
    '''
    return len(histogram)


def main():
    '''Tests generate_histogram_dict() and unique_words().'''
    with open('./texts/test.txt') as file:
        my_text = file.read()

    my_histogram = generate_histogram_dict(my_text)
    my_unique_words = unique_words(my_histogram)

    print(my_histogram)
    print(my_unique_words)


if __name__ == '__main__':
    main()

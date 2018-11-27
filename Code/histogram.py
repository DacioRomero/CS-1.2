'''Generates a histogram of the frequency of words in a text.'''
import re
import sample

# Matches latin-esque words
WORD_RE = re.compile(r'[a-zA-Z]+(?:\'[a-z]+)?')


# TODO: Move to sample.py
def dict_sample(the_histogram):
    '''Gets a random, weighted sample from a histogram.

    Args:
        the_histogram: The histogram dict to draw from.

    Returns:
        A random key from the_histogram based on its weight.
    '''
    # https://stackoverflow.com/a/4019648/10336544
    # Convert dictionary to tuples of keys and values.
    return sample.random_choice(*zip(*the_histogram.items()))


def dict_samples(the_histogram, k=1):
    '''Gets random, weighted samples from a histogram.

    Args:
        the_histogram: The histogram dict to draw from.

    Returns:
        A list of random keys from the_histogram based on their weights.
    '''
    # https://stackoverflow.com/a/4019648/10336544
    # Convert dictionary to tuples of keys and values and pass as arguments
    return sample.random_choices(*zip(*the_histogram.items()), k=k)


# TODO: Separate different histograms into classes
def dict_generate(seq):
    '''Generates a histogram of a string.

    Args:
        seq: An iterable or string to generate from.

    Returns:
        A dictionary of unique words each with a value of their occurences.
    '''
    if isinstance(seq, str):
        words = get_words(seq)
    else:
        words = seq

    histogram = {}

    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram


def generate_ll(seq):
    '''Generates a histogram of a string.

    Args:
        seq: An iterable or string to generate from.

    Returns:
        A list of lists in the format [[word, occurences], ...].
    '''
    if isinstance(seq, str):
        words = get_words(seq)
    else:
        words = seq

    words.sort()

    histogram = []

    for index, word in enumerate(words):
        if index > 0 and word == words[index - 1]:
            histogram[-1][1] += 1
        else:
            histogram.append([word, 1])

    return histogram


def generate_lt(seq):
    '''Generates a histogram of a string.

    Args:
        seq: An iterable or string to generate from.

    Returns:
        A list of tuples in the format [(word, occurences), ...].
    '''
    if isinstance(seq, str):
        words = get_words(seq)
    else:
        words = seq

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


# TODO: Separate into another file
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
    '''Tests dict_generate() and unique_words().'''
    with open('./texts/test.txt') as file:
        my_text = file.read()

    my_histogram = dict_generate(my_text)
    my_unique_words = unique_words(my_histogram)

    print(my_histogram)
    print(my_unique_words)


if __name__ == '__main__':
    main()

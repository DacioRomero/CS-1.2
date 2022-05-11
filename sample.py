'''Display a random word from input based on frequency'''
import random
import sys
import histogram

def random_choices(seq, weights=None, cum_weights=None, k=1):
    '''Picks a weighted random choice from a histogram.

    Mimics random.choice.

    Args:
        seq: The histogram in dictionary format to choose from.

    Returns:
        A random choice using the count as the weights for probability.
    '''
    # Total of all previous weight and current weight at current weight.
    # Makes comparisions easier.
    cum_weights = convert_weights(weights)

    return [random_choice(seq, cum_weights=cum_weights) for _ in range(k)]

def random_choice(seq, weights=None, cum_weights=None):
    '''Chooses a random token from an iterable.

    Mimics random.choice with weights. Converts weights to cum_weights.

    Args:
        seq: An iterable sequence.
        weights: An iterable of ints or floats in any order.
        cum_weights: An iterable of numbers in ascending order.

    Raises:
        ValueError: If sample is out of range or lengths are unequal.
    '''
    equal_len_err = ValueError('all provided iterables must be equal length')

    # Convert weights to cumulative weights.
    if weights is not None:
        if len(seq) != len(weights):
            raise equal_len_err

        cum_weights = convert_weights(weights)
    elif cum_weights is not None:
        if len(seq) != len(cum_weights):
            raise equal_len_err

    choice = None

    # Choose completey randomly if no weights given.
    if cum_weights is None:
        choice = random.choice(seq)
    else:
        max_weight = cum_weights[-1]
        sample = random.random() * max_weight  # [0, max_weight)

        if sample < 0 or sample >= max_weight:
            raise ValueError('sample generated out of range')

        # Loop over the seq and *cumulative* weights together
        for item, cum_weight in zip(seq, cum_weights):
            # sample is in the range of this weight
            if sample < cum_weight:
                choice = item
                break

    return choice

def convert_weights(weights):
    '''Converts arbitrary weights

    Args:
        weights: An iterable of numbers to convert

    Returns:
        The cumulative weights, a list in ascending order'''
    cum_weights = []
    current_total = 0

    for weight in weights:
        current_total += weight
        cum_weights.append(current_total)

    return cum_weights

def main():
    '''Tests histogram_samples().'''
    my_histogram = histogram.generate_histogram_dict(' '.join(sys.argv[1:]))
    samples = histogram_samples(my_histogram, k=100000)
    print(histogram.generate_histogram_dict(samples))

if __name__ == '__main__':
    main()

import random
import sys
import sample
import re
from dictogram import Dictogram
from queue import Queue

class MarkovChain(dict):
    def __init__(self, words, order=1):
        super(MarkovChain, self)
        self.order = order
        self._generate(words)

    # TODO: Use Queue
    def _generate(self, words):
        words = tuple(words)
        for i in range(len(words) - self.order):
            current = words[i:i+self.order]
            next = words[i + self.order]

            if current not in self:
                self[current] = Dictogram()

            self[current].add_count(next)

    def walk(self, num_sentences=10):
        # Get random starting point from keys
        starting_points = list(filter(lambda x: x[0] is None, self.keys()))
        chain = list(random.choice(starting_points))
        queue = Queue(chain)

        sentences = 0
        while sentences < num_sentences:
            prev_words = tuple(queue.items())
            new_word = self[prev_words].sample()

            queue.enqueue(new_word)
            queue.dequeue()

            if new_word is None:
                sentences += 1
            else:
                chain.append(new_word)

        phrase = []
        for segment in chain[1:]:
            # Word
            if re.match(r'\w+', segment) is None:
                phrase[-1] += segment
            else:
                phrase.append(segment)

        result = ' '.join(phrase)
        return result

def get_words(corpus):
    '''Get words in corpus with None indicating the start and end of sentences'''
    sentences = re.findall(r'\w.+?[.?!:]+', corpus)

    segment_matcher = re.compile(r'\w+(?:-\w+|[’\']\w+)?|\S+')
    segments = []
    for sentence in sentences:
        new_segments = segment_matcher.findall(sentence)
        if new_segments is not None:
            segments.extend(new_segments)
            segments.append(None)

    return segments

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Generate a sentence based on a markov chain')

    parser.add_argument('text', type=str, help='the text to read from')
    parser.add_argument('--order', '-o', metavar='O', type=int, default=3,
                        help='the depth to parse')
    parser.add_argument('--num', '-n', metavar='N', type=int, default=10,
                        help='the number of words in the generated sentence')

    args = parser.parse_args()

    with open(args.text) as file:
        corpus = file.read()

    words = get_words(corpus)
    chain = MarkovChain(words, order=args.order)

    sentence = chain.walk(args.num)

    print(sentence)


if __name__ == '__main__':
    main()

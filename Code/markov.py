import random
import sys
import histogram
import sample
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

    def walk(self, num_words=10):
        # Get random starting point from keys
        words = list(random.choice(list(self.keys())))
        queue = Queue(words)

        for _ in range(num_words - self.order):
            prev_words = tuple(queue.items())
            new_word = self[prev_words].sample()

            words.append(new_word)
            queue.enqueue(new_word)

            queue.dequeue()

        return ' '.join(words)

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

    words = histogram.get_words(corpus)
    chain = MarkovChain(words, order=args.order)

    sentence = chain.walk(args.num)

    print(sentence)


if __name__ == '__main__':
    main()

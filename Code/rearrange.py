'''Displays a shuffled version of a provided list without mutation.'''
import random
import sys


def randomize_list(input_list):
    '''Rearrange a list without mutation.

    Args:
        input_list: A list to be reversed.

    Returns:
        The randomly rearranged list.
    '''
    output_list = input_list[:]
    # TODO: Write own "shuffle" function
    random.shuffle(output_list)
    return output_list

def main():
    '''Tests randomize_list().'''
    print(' '.join(randomize_list(input_list=sys.argv[1:])))

if __name__ == '__main__':
    main()

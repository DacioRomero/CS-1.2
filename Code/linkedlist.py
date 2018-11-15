#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) loops through all elements regardless to count."""
        count = 0 # O(1)
        node = self.head # O(1)

        while node is not None: # O(n)
            count += 1 # O(1)
            node = node.next # O(1)

        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) no loops because tail is tracked."""
        item_node = Node(item) # O(1)

        if self.is_empty(): # O(1)
            self.head = item_node # O(1)
        else: # O(1)
            # Set old tail to point to new tail
            self.tail.next = item_node # O(1)

        self.tail = item_node # O(1)


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) no loops because head is tracked."""
        item_node = Node(item) # O(1)

        if self.is_empty(): # O(1)
            self.tail = item_node # O(1)
        else: # O(1)
            item_node.next = self.head # O(1)

        self.head = item_node # O(1)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) no loops if head matches.
        Worst case running time: O(n) all elements looped if last node
            matches or none do."""
        node = self.head # O(1)

        while node is not None: # O(n) or O(1)
            if quality(node.data): # O(1)
                return node.data # O(1)

            node = node.next # O(1)

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) no loops if empty, head matches, or
            head.next matches.
        Worst case running time: O(n) loops otherwise."""
        # Skip iteration if self.head is not set
        if not self.is_empty(): # O(1)
            if self.head.data == item: # O(1)
                # Reset if length is one
                if self.head is self.tail: # O(1)
                    self.head = None # O(1)
                    self.tail = None # O(1)
                else:
                    self.head = self.head.next # O(1)

                return
            else:
                node = self.head # O(1)

                while node.next is not None: # O(1) or O(n) - return
                    # If the node after this one matches
                    if node.next.data == item: # O(1)
                        # Set self.tail to node if node.next is self.tail
                        if node.next is self.tail: # O(1)
                            self.tail = node # O(1)

                        node.next = node.next.next # O(1)

                        return # O(1)

                    node = node.next # O(1)

        raise ValueError('Item not found: {}'.format(item)) # O(1)


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()

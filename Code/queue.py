from linkedlist import LinkedList

class Queue:
    def __init__(self, items=None):
        self.linkedlist = LinkedList(items)

    def enqueue(self, item):
        self.linkedlist.append(item)

    def dequeue(self):
        if self.linkedlist.head is not None:
            item = self.linkedlist.head.data
            self.linkedlist.head = self.linkedlist.head.next
            return item

    def items(self):
        return self.linkedlist.items()

def main():
    queue = Queue(['a', 'b', 'c'])

    print('Enqueue "d"')
    queue.enqueue('d')
    print(queue.items())

    print('Dequeue')
    print(queue.dequeue())
    print(queue.items())


if __name__ == "__main__":
    main()

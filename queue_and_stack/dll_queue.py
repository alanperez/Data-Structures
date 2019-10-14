from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size = self.storage.length
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            node_removed = self.storage.remove_from_head()
            self.size = self.storage.length
            return node_removed
        else:
            return None

    def len(self):
        return self.storage.length

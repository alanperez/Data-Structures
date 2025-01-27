from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.storage = dict()
        self.order = DoublyLinkedList()
        self.size = 0
        self.limit = limit
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # Get the item or handle none
        # Move to front
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return
        if self.size == self.limit:
            node = self.order.head  # Get the oldest node in the cache
            node_value = node.value  # Tuple storing (key, value)
            key_for_dict = node_value[0]  # get key for dict
            del self.storage[key_for_dict]
            self.order.remove_from_head()
            # del self.storage[self.order.remove_from_head()[0]] # Another way to write above 2 lines
            self.size -= 1

        # Adds the given key-value pair to the cache.
        # Add to LL at the tail
        self.order.add_to_tail((key, value))
        # Add to dictionary
        self.storage[key] = self.order.tail
        self.size += 1

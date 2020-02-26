import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.size = 0
        self.limit = limit
        self.dll = DoublyLinkedList() # holds key-value entries in the correct order 
        self.storage = {} # provides fast access to every node in the cache

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            element = self.storage[key]
            self.dll.move_to_front(element)
            return self.dll.head.value
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
        if self.size < self.limit:
            # if size greater than limit
            # add value to head of dll

            self.dll.add_to_head(value)
            self.storage[key] = self.dll.head
            self.size += 1
        elif key in self.storage:
            # if key is already in storage
            # delete current node with that key
            # add new value to head of dll
            # set head node to key

            node = self.storage[key]
            self.dll.delete(node)
            self.dll.add_to_head(value)
            self.storage[key] = self.dll.head
        else:
            # remove tail key from storage
            # else remove least recent used element
            # make new insertion the most recent

            el = ''
            for k,v in self.storage.items():
                if v == self.dll.tail:
                    el = k
            del self.storage[el]

            self.dll.remove_from_tail()
            self.dll.add_to_head(value)
            self.storage[key] = self.dll.head
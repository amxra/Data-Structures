from doubly_linked_list import DoublyLinkedList #import
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0 
        self.order = DoublyLinkedList()
        self.storage = dict()
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage: # if key is in dictionary
            node = self.storage[key] #extract node from storage at the key
            self.order.move_to_end(node)#move the key to end of the order
            return node.value[1] #return value of the value of the node
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
        #create a node if key is not found
        #move node to front if key found
        #if full remove last node from linked list and disctionary
        if key in self.storage: # if key is in storage/dict
            node = self.storage[key] #extract the node from storage
            node.value= (key, value) #set node to kvp
            self.order.move_to_end(node) #call the move to end from dll
            return
        if self.size == self.limit: #if its same as limit(10)
            del self.storage[self.order.head.value[0]] #delete the storage at the heads value key
            self.order.remove_from_head() #remove from head
            self.size -= 1   #decrement size
        #if both cases are false
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1 #increment size
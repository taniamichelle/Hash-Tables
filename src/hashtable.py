# '''
# Linked List hash table key/value pair.
# Because the hash table uses separate chaining, each bucket 
# will actually contain a LL of nodes containing the objects 
# stored at that index. When we need to look up one of those 
# items, we iterate the list until we find the Node matching
# the requested key.This is one method of collision resolution.
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  #determines the size of our internal array
        self.storage = [None] * capacity #internal array (stores each inserted value in a “bucket” based on key provided)
        # linked = LinkedPair()

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        size = 0  # Number of elements that have been inserted
        size += 1   # 1) Increment size
        index = self._hash(key)  # 2) Compute index of key
        node = self.storage[index]  # Go to the node corresponding to the hash
        if node is None:  # 3) If bucket is empty:
            self.storage[index] = LinkedPair(key, value)  # create node, add it
            return
        self.prev = node  # 4) Collision: Iterate to the end of LL at provided index
        while node is not None:
            self.prev = node
            node = node.next
        self.prev = LinkedPair(key, value)  # Add a new node at the end of the list with provided key/value


    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        size = 0  # Number of elements that have been inserted
        index = self._hash(key)  # 1) Compute hash
        node = self.storage[index]
        self.prev = None
        while node is not None and node.key != key:  # 2) iterate to requested node
            self.prev = node
            node = node.next
        if node is None:  # if requested node not found: 
            print("Warning: key not found")
            return
        else:  # if key found:
            size -= 1
            result = node.value
            if self.prev is None:  # Delete this element from LL
                node = None
            else:
                self.prev.next = self.prev.next.next
            return result  # Return deleted value


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Return None if the key is not found.
        Fill this in.
        '''
        index = self._hash(key)  # 1) Compute hash
        node = self.storage[index]  # 2) Go to first node in LL at bucket
        while node is not None and node.key != key:  # 3) Traverse LL at this node
            node = node.next
        if node is None:  # If node not found:
            return None
        else:  # If found:
            return node.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        count = 0
        self.capacity *= 2  # double the capacity
        new_storage = [None] * self.capacity  # define new_storage
        for i in range(count):  # copy stored elements into new table
            new_storage[i] = self.storage[i] 
        self.storage = new_storage  # set new_storage equal to storage
        return self._hash
        


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

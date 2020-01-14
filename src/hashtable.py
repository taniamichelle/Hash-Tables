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
    A hash table with `capacity` buckets that accepts string keys.
    storage: internal array that stores each inserted value in a 
    `bucket` based on key provided
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # determines the size of our internal array
        self.storage = [None] * capacity
        self.size = 0  # Number of elements that have been inserted

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
        hashed_key = self._hash_mod(key)  # 2) Compute index of key
        if self.storage[hashed_key] is not None:  # 4) Collision
            new_pair = LinkedPair(key, value)
            new_pair.next = self.storage[hashed_key]
            self.storage[hashed_key] = new_pair
        else:  # 3) If bucket is empty:
            self.storage[hashed_key] = LinkedPair(
                key, value)  # create & add node
            self.size += 1   # 1) Increment size each time insert method is called

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        hashed_key = self._hash_mod(key)  # 1) Compute hash

        if self.storage[hashed_key] is None:  # if requested node not found
            print("Warning: key not found")
        else:
            node = self.storage[hashed_key]
            prev_node = None
            while node:  # while there IS a node, check if curr key matches target key
                if node.key != key:  # if current key is NOT the target key:
                    prev_node = node  # 2) iterate to next node by changing pointers
                    node = node.next
                else:  # if current is the target key, check where we are in LL:
                    if node.next is None:  # if Linked pair IS at end of LL
                        if prev_node is None:  # if there is NOT a prev node
                            # point last node to None
                            self.storage[hashed_key] = None
                            self.size -= 1  # decrement size
                            return
                        else:  # if there IS a prev node
                            prev_node.next = None
                            self.size -= 1  # decrement size
                            return
                    else:  # if Linked pair is NOT at end of LL
                        if prev_node is None:  # if Linked pair is at start of LL
                            self.storage[hashed_key] = node.next
                            self.size -= 1
                            return
                        else:  # if Linked pair is in middle of LL
                            prev_node.next = node.next  # point prev node to node after removed node
                            self.size -= 1
                            return
            return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Return None if the key is not found.
        Fill this in.
        '''
        hashed_key = self._hash_mod(key)  # 1) Compute hash
        node = self.storage[hashed_key]  # 2) Go to first node in LL at bucket
        while node is not None:  # 3) Traverse LL at this node
            if node.key != key:  # if current key is NOT target key
                node = node.next    # iterate to next node
            else:   # if current key IS target key
                return node.value   # return the current value
        return None  # If key not found return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        self.capacity *= 2  # double the capacity
        new_storage = self.storage  # create temp storage: new_storage
        self.storage = [None] * self.capacity  # expanding storage
        for each_bucket in new_storage:  # for each bucket in new_storage array
            curr_bucket = each_bucket  # create iterator for each bucket
            while curr_bucket:  # while we still have elements in our buckets
                self.insert(curr_bucket.key, curr_bucket.value)
                curr_bucket = curr_bucket.next


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

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

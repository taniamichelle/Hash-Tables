class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0 # Count is how much is currently used
        self.capacity = capacity # ho much is currently allocated
        self.storage = [None] * self.capacity
    
    def insert(self, index, value): 
        if self.count == self.capacity:
            # print("Error: array is full")
            self.resize
            return

            # Shift everything to the right
            for i in range(self.count, index):
                self.storage[i] = self.storage[i-1]

            # Insert our value
            self.storage[index] = value
            self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def resize(self):  # make another block of memory w/ double the capacity
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i] # copy over stored items 
        self.storage = new_storage # move pointer to new_storage

    def replace(self, index, value):
        self.storage[index] = value

    def add_to_front(self, value):
        self.insert(0, value) # insert value at 0 index (after moving everything right one)

    def slice(self, beginning_index, end_index): # default end value
        # need beginning and end index
        # create subarray to store value 
        # copy beginning to end to subarray
        # decide what happens to original array- remove it or leave it alone?
        # return subarray

myArray = DynamicArray(4)
print(myArray)
import time

# e-max - Oldschool text editor that Tim is using


class dynamic_array:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity

    def insert(self, index, value):
        # Check for size first
        if self.count == self.capacity:
            print('array is full')
            return
        # adjust the array space freeing up the memory at "index"
        for idx in range(self.count, 0, -1):
            self.storage[idx] = self.storage[idx - 1]

        # add a value at index
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        # if the array is full, double the array's size
        if self.count == self.capacity:
            self.double_size()

        # add the value to the end
        self.storage[self.count] = value
        self.count += 1

    def double_size(self):
        # double capacity and create a new array with the
        # new capacity
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity

        # Copy the old array
        for i in range(self.count):
            new_arr[i] = self.storage[i]

        self.storage = new_arr

# O(n^2)


def add_to_front(n):
    x = []
    for i in range(n):
        x.insert(i, n-1)
    return x

# O(n)


def add_to_back(n):
    x = []
    for i in range(n):
        x.append(i)
    return x


def preallocate(n):
    x = [None] * n
    for i in range(n):
        x[i] = i
    return x


n = 5000

start_time = time.time()
add_to_back(n)
end_time = time.time()

print("Time to add to back = ", end_time - start_time)

start_time = time.time()
add_to_front(n)
end_time = time.time()

print("Time to add to front = ", end_time - start_time)


def djb2(key):
    # start with a high prime number
    hash_value = 5381

    # scramble this bitch up
    for char in key:
        hash_value = hash_value + (hash_value << 5) + char

    return hash_value

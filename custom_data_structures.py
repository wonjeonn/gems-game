class Stack:
    def __init__(self, cap=10):
        self.list_capacity = cap
        self.list_size = 0
        self.list_data = [None] * self.list_capacity

    def capacity(self):
        return self.list_capacity

    def push(self, data):
        if self.list_size == self.list_capacity:
            new_capacity = self.list_capacity * 2
            new_data = [None] * new_capacity
            for i in range(self.list_size):
                new_data[i] = self.list_data[i]
            self.list_data = new_data
            self.list_capacity = new_capacity

        self.list_data[self.list_size] = data
        self.list_size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        self.list_size -= 1
        value = self.list_data[self.list_size]
        self.list_data[self.list_size] = None
        return value

    def get_top(self):
        if self.is_empty():
            return None
        return self.list_data[self.list_size - 1]

    def is_empty(self):
        return self.list_size == 0

    def __len__(self):
        return self.list_size


class Queue:
    def __init__(self, cap=10):
        self.list_capacity = cap
        self.list_size = 0
        self.front = 0
        self.list_data = [None] * self.list_capacity

    def capacity(self):
        return self.list_capacity

    def enqueue(self, data):
        if self.list_size == self.list_capacity:
            new_capacity = self.list_capacity * 2
            new_data = [None] * new_capacity
            for i in range(self.list_size):
                new_data[i] = self.list_data[(
                    self.front + i) % self.list_capacity]
            self.list_data = new_data
            self.front = 0
            self.list_capacity = new_capacity

        rear = (self.front + self.list_size) % self.list_capacity
        self.list_data[rear] = data
        self.list_size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        value = self.list_data[self.front]
        self.list_data[self.front] = None
        self.front = (self.front + 1) % self.list_capacity
        self.list_size -= 1
        return value

    def get_front(self):
        if self.is_empty():
            return None
        return self.list_data[self.front]

    def is_empty(self):
        return self.list_size == 0

    def __len__(self):
        return self.list_size


class Deque:
    def __init__(self, cap=10):
        self.list_capacity = cap
        self.list_size = 0
        self.front = 0
        self.list_data = [None] * self.list_capacity

    def capacity(self):
        return self.list_capacity

    def push_front(self, data):
        if self.list_size == self.list_capacity:
            new_capacity = self.list_capacity * 2
            new_data = [None] * new_capacity
            for i in range(self.list_size):
                new_data[i] = self.list_data[(
                    self.front + i) % self.list_capacity]
            self.list_data = new_data
            self.front = 0
            self.list_capacity = new_capacity

        self.front = (self.front - 1) % self.list_capacity
        self.list_data[self.front] = data
        self.list_size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        value = self.list_data[self.front]
        self.list_data[self.front] = None
        self.front = (self.front + 1) % self.list_capacity
        self.list_size -= 1
        return value

    def push_back(self, data):
        if self.list_size == self.list_capacity:
            new_capacity = self.list_capacity * 2
            new_data = [None] * new_capacity
            for i in range(self.list_size):
                new_data[i] = self.list_data[(
                    self.front + i) % self.list_capacity]
            self.list_data = new_data
            self.front = 0
            self.list_capacity = new_capacity

        rear = (self.front + self.list_size) % self.list_capacity
        self.list_data[rear] = data
        self.list_size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        rear = (self.front + self.list_size - 1) % self.list_capacity
        value = self.list_data[rear]
        self.list_data[rear] = None
        self.list_size -= 1
        return value

    def get_front(self):
        if self.is_empty():
            return None
        return self.list_data[self.front]

    def get_back(self):
        if self.is_empty():
            return None
        rear = (self.front + self.list_size - 1) % self.list_capacity
        return self.list_data[rear]

    def is_empty(self):
        return self.list_size == 0

    def __len__(self):
        return self.list_size

    def __getitem__(self, k):
        if k < 0 or k >= self.list_size:
            raise IndexError('Index out of range')
        return self.list_data[(self.front + k) % self.list_capacity]

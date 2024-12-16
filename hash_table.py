class HashTable:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity=32):
        self._capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def insert(self, key, value):
        index = self._get_hash(key)
        new_node = self.Node(key, value)
        current_node = self.table[index]

        if current_node:
            while current_node:
                if current_node.key == key:
                    return False
                if not current_node.next:
                    current_node.next = new_node
                    self.size += 1
                    if self.size / self._capacity > 0.7:
                        self._resize()
                    return True
                current_node = current_node.next
        else:
            self.table[index] = new_node
            self.size += 1
            if self.size / self._capacity > 0.7:
                self._resize()
            return True

    def modify(self, key, value):
        index = self._get_hash(key)
        current_node = self.table[index]
        while current_node:
            if current_node.key == key:
                current_node.value = value
                return True
            current_node = current_node.next
        return False

    def remove(self, key):
        index = self._get_hash(key)
        current_node = self.table[index]
        prev_node = None

        while current_node:
            if current_node.key == key:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.table[index] = current_node.next
                self.size -= 1
                return True
            prev_node = current_node
            current_node = current_node.next
        return False

    def search(self, key):
        index = self._get_hash(key)
        current_node = self.table[index]
        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        return None

    def capacity(self):
        return self._capacity

    def __len__(self):
        return self.size

    def _get_hash(self, key):
        return hash(key) % self._capacity

    def _resize(self):
        new_capacity = self._capacity * 2
        new_table = [None] * new_capacity

        for node in self.table:
            current_node = node
            while current_node:
                index = hash(current_node.key) % new_capacity
                new_node = self.Node(current_node.key, current_node.value)
                if new_table[index]:
                    temp_node = new_table[index]
                    while temp_node.next:
                        temp_node = temp_node.next
                    temp_node.next = new_node
                else:
                    new_table[index] = new_node
                current_node = current_node.next

        self._capacity = new_capacity
        self.table = new_table

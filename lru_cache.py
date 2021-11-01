"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""
from collections import OrderedDict

# Approach 1 : Use OrderedDict data structure available in Python / LinkedHashmap available in Java


class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:

        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Approach 2 Use Hashmap + DoubleLinkedList


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache1:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_head(self, node):
        head_next = self.head.next
        node.prev = self.head
        node.next = head_next
        head_next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._move_to_head(node)
        return node.key

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node = self._cache[key]
            new_node = DLinkedNode(key, value)
            self._remove_node(node)
            self._move_to_head(new_node)
            node.value = value
            self._cache[key] = new_node
        else:
            new_node = DLinkedNode(key, value)
            self._cache[key] = new_node
            self._move_to_head(new_node)
            if len(self._cache) > self._capacity:
                node = self.tail.prev
                self._remove_node(node)
                del self._cache[node.key]


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache1(2)
obj.put(1, 10)
obj.put(2, 10)
obj.get(2)
obj.put(3, 10)
print(obj.get(1))

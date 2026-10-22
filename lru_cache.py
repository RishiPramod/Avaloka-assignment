class _Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")

        self.capacity = capacity
        self.nodes = {}

        # Entries are ordered from most to least recently used.
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Detach a node from its current position."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        """Place a node in the most recently used position."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        node = self.nodes.get(key)

        if node is None:
            return -1

        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        node = self.nodes.get(key)

        if node is not None:
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return

        if len(self.nodes) == self.capacity:
            least_recent = self.tail.prev
            self._remove(least_recent)
            del self.nodes[least_recent.key]

        node = _Node(key, value)
        self.nodes[key] = node
        self._add_to_front(node)


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 10)
    cache.put(2, 20)
    print(cache.get(1))  # Accessing key 1 makes it most recent.

    cache.put(3, 30)     # Evicts key 2.
    print(cache.get(2))

    cache.put(1, 100)    # Updates key 1 and marks it most recent.
    cache.put(4, 40)     # Evicts key 3.

    print(cache.get(3))
    print(cache.get(1))
    print(cache.get(4))
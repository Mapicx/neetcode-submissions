from collections import defaultdict

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0

    def length(self):
        return self.size

    def pushright(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

        self.size += 1

    def pop(self, node):
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev

        node.prev = None
        node.next = None

        self.size -= 1

    def popleft(self):
        if self.size == 0:
            return None

        node = self.left.next
        self.pop(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minFreq = 0

        # key -> node
        self.nodeMap = {}

        # freq -> DLL
        self.listMap = defaultdict(LinkedList)

    def updateFreq(self, node):
        freq = node.freq

        # Remove node from old frequency list
        self.listMap[freq].pop(node)

        # If this was the minimum frequency list and it becomes empty
        if freq == self.minFreq and self.listMap[freq].length() == 0:
            self.minFreq += 1

        # Increase frequency
        node.freq += 1

        # Add to new frequency list
        self.listMap[node.freq].pushright(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]
        self.updateFreq(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        # Key already exists
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.updateFreq(node)
            return

        # Cache full
        if len(self.nodeMap) == self.cap:
            node = self.listMap[self.minFreq].popleft()
            del self.nodeMap[node.key]

        # Insert new node
        node = ListNode(key, value)

        self.nodeMap[key] = node
        self.listMap[1].pushright(node)

        self.minFreq = 1
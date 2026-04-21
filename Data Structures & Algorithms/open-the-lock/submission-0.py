from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        if target == "0000":
            return 0
        
        queue = deque([("0000", 0)])
        visited = set(deadends)
        turns = 0
        if "0000" in visited:
            return -1
        def children(node):
            res = []
            for i in range(4):
                digit = str((int(node[i]) + 1) % 10)
                res.append(node[:i] + digit + node[i+1:])
                digit = str((int(node[i]) - 1 + 10) % 10)
                res.append(node[:i] + digit + node[i+1:])
            return res


        while queue:
            node, turns = queue.popleft()
            if node == target:
                return turns
            for child in children(node):
                if child not in visited:
                    queue.append((child, turns + 1))
                    visited.add(child)
        return -1

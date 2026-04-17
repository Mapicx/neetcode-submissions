class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_new = {}

        def dfs(node):
            if node in old_new:
                return old_new[node]

            copy = Node(node.val)
            old_new[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)

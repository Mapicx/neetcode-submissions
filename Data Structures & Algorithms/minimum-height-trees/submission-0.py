class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            farthest_node = node
            max_dist = 0

            for nei in adj[node]:
                if nei == parent:
                    continue

                nei_node, nei_dist = dfs(nei, node)

                if nei_dist + 1 > max_dist:
                    max_dist = nei_dist + 1
                    farthest_node = nei_node

            return farthest_node, max_dist

        node_a, _ = dfs(0, -1)
        node_b, _ = dfs(node_a, -1)
        path = []

        def find_path(node, parent):
            if node == node_b:
                path.append(node)
                return True

            for nei in adj[node]:
                if nei == parent:
                    continue

                if find_path(nei, node):
                    path.append(node)
                    return True

            return False

        find_path(node_a, -1)
        path.reverse()
        L = len(path)

        if L % 2 == 1:
            return [path[L // 2]]
        else:
            return [path[L // 2 - 1], path[L // 2]]
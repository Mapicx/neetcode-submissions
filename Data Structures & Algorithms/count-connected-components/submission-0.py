class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei)

        components = 0
        for num in range(n):
            if num not in visit:
                dfs(num)
                components += 1

        return components

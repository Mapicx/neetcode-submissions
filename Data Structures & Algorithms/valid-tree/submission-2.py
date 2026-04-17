class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i : [] for i in range(n)}
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)  
        cycle = set()

        def dfs(node, parent):
            if node in cycle:
                return False
            cycle.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if dfs(nei, node) == False:
                    return False
            return True

        if dfs(0, -1) == False or len(cycle) != n:
            return False
        return True
            

from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))       
            graph[v].append((u, 1 / val))
        
        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            visit = set()
            queue = deque()
            queue.append((src, 1))

            while queue:
                node , val = queue.popleft()
                if node == dst:
                    return val
                visit.add(node)
                for nei, weight in graph[node]:
                    if nei not in visit:   
                        visit.add(nei)
                        queue.append((nei, val * weight))
            return -1.0
        res = []
        for u,v in queries:
            res.append(bfs(u,v))
        return res

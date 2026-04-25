class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}
        n = len(edges)
        for i in range(1, n+1):
            par[i] = i
            rank[i] = 0
        
        def find(node):
            parent = par[node]
            while parent != par[parent]:
                par[parent] = par[par[parent]]
                parent = par[parent]
            return parent
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]



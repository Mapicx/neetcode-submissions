class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        
        for s, d, t in times:
            adj[s].append([d, t])
        
        min_time = {}
        minheap = [[0, k]]

        while minheap:
            t1, n1 = heapq.heappop(minheap)
            if n1 in min_time:
                continue

            min_time[n1] = t1

            for n2, t2 in adj[n1]:
                if n2 not in min_time:
                    heapq.heappush(minheap, [t1+t2, n2])
        
        if len(min_time) != n:
            return -1
        return max(min_time.values())

            
        
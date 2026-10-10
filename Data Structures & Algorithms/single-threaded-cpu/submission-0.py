import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        heap = []
        i = 0
        time = 0
        n = len(tasks)
        tasks = sorted(
            (enqueuetime, processingtime, index)
            for index, (enqueuetime, processingtime) in enumerate(tasks)
        )

        while i < n or heap:
            if i < n and time < tasks[i][0]:
                time = tasks[i][0]
            
            while i < n and tasks[i][0] <= time:
                enqueuetime, processingtime, index = tasks[i]
                heapq.heappush(heap, (processingtime, index, enqueuetime))
                i += 1
            
            processingtime, index, _= heapq.heappop(heap)
            res.append(index)
            time += processingtime
        return res
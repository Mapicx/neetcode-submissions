class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)        
        
        queue = deque()
        time = 0
        while heap or queue:
            time += 1
            if not heap:
                time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt != 0:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                new_cnt = queue.popleft()[0]        
                heapq.heappush(heap, new_cnt)

        return time

            



        
        

        
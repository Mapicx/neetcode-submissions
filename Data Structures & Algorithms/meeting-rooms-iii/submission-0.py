class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        avail = [num for num in range(n)]
        used = [] #end_time, room
        count = [0] * n

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(avail, room)

            if not avail:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(avail, room)
            
            room = heapq.heappop(avail)
            heapq.heappush(used, (end, room))
            count[room] += 1
        return count.index(max(count))



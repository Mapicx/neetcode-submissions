class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x: x[1])
        heap = []
        passangers = 0
        for numpass, start, end in trips:

            while heap and heap[0][0] <= start:
                passangers -= heapq.heappop(heap)[1]

            passangers += numpass
            if passangers > capacity:
                return False
            heapq.heappush(heap, [end, numpass])
        return True
            



        
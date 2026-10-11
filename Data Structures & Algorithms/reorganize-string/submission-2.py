import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxheap)

        res = ""
        prev = None
        while prev or maxheap:
            if prev and not maxheap:
                return ""
            cnt, char = heapq.heappop(maxheap)
            cnt += 1
            res += char
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
             
            if cnt != 0:
                prev = [cnt, char]

        return res
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def find_time(rate: int) -> int:
            total_time = 0
            for bananas in piles:
                total_time += (bananas + rate - 1) // rate 
            return total_time

        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            mid = (left + right) // 2
            time = find_time(mid)

            if time <= h:
                answer = mid 
                right = mid - 1
            else:
                left = mid + 1

        return answer

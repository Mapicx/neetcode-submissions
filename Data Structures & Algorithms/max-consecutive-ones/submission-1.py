class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, maxlen = float("-inf"),0
        for num in nums:
            if num == 1:
                maxlen += 1
                res = max(res, maxlen)
            else:
                maxlen = 0
        return res if res != float("-inf") else 0
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        perfixSums = {0 : 1}

        for n in nums:
            currSum += n
            diff = currSum - k
            
            res += perfixSums.get(diff, 0)
            perfixSums[currSum] = 1 + perfixSums.get(currSum, 0)
        return res

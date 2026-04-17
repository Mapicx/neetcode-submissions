class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currmax = 1
        currmin = 1

        for num in nums:
            tmp = currmax * num
            currmax = max(num * currmax, num * currmin, num)
            currmin = min(num, tmp, num * currmin)
            res = max(currmax, res)
        return res


        
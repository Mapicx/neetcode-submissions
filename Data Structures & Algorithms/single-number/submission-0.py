class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a ^ a = 0 
        # a ^ 0 = a 
        # so if we get res and xored it with all the elemnts form the arr we will 
        # get the single element that has not appeared twice
        res = 0
        for num in nums:
            res = res ^ num
        return res
        
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        target = len(nums) // 3

        for key in count:
            if count[key] > target:
                res.append(key)
        return res

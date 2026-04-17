class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        is_used = [False] * len(nums)

        def recur(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if is_used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not is_used[i - 1]:
                    continue
                curr.append(nums[i])
                is_used[i] = True
                recur(curr)
                is_used[i] = False
                curr.pop()

        recur([])
        return res

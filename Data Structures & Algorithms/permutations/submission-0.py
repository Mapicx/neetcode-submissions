class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        is_used = [False] * len(nums)

        def recur(is_used, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(is_used)):
                if is_used[i] == False:
                    curr.append(nums[i])
                    is_used[i] = True
                    recur(is_used, curr)
                    is_used[i] = False
                    curr.pop()
            


        recur(is_used,[])
        return res


        
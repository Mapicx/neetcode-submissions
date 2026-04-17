class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        seen = set()  

        def dfs(i, curr, total):
            if total == target:
                key = tuple(sorted(curr))  
                if key not in seen:
                    seen.add(key)
                    res.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            # take current number
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()

            # skip current number
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res

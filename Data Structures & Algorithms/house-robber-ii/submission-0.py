class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def solve(l, r):
            memo = {}

            def dfs(i):
                if i > r:
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
                return memo[i]
            return dfs(l)
        
        return max(solve(0, n-2), solve(1, n-1))
                
        
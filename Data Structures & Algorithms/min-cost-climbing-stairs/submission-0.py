class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if len(cost) == 2:
            return min(cost[0], cost[1])
        one, two = 0,0
        for i in range(len(cost) - 1, -1, -1):
            tmp = two
            two = cost[i] + min(one, two)
            one = tmp
        return min(one, two)

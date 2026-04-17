class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if (sum(matchsticks) % 4) != 0:
            return False
        target_len = sum(matchsticks) / 4
        sides = [0] * 4
        matchsticks.sort(reverse=True) # for optimisation to see if the biggest element > target_len then return false

        def backtrack(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for side in range(4):
                if sides[side] + matchsticks[i] <= target_len:
                    sides[side] += matchsticks[i]
                    if backtrack(i + 1) == True:
                        return True
                    sides[side] -= matchsticks[i]
            return False
        return backtrack(0)


                
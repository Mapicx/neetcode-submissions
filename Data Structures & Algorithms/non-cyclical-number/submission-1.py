class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while num not in seen:
            seen.add(num)
            num = sum(int(d)**2 for d in str(num))
            if num == 1:
                return True
        return False
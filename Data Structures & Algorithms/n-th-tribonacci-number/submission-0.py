class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2 and n != 0:
            return 1
        
        a, b, c = 0,1,1
        for _ in range(3, n+1):
            a, b, c = b, c, c + b + a
        return c
        
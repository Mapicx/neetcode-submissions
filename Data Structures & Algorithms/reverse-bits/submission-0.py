class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n, "032b")
        return int(b[::-1], 2)
            
        
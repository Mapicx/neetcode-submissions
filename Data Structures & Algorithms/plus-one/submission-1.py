class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # hack method
        s = ''.join(map(str, digits))
        num = int(s)
        num += 1
        num = str(num)
        return [int(ch) for ch in num]
        
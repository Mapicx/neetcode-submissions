class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        count = 0
        for num in range(n + 1):
            while num > 0:
                if num & 1 == 1:
                    count += 1
                num = num >> 1
            res.append(count)
            count = 0
        return res

        
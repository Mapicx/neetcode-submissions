class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def recur(i, curr):
            if i > n:
                if len(curr) == k:
                    res.append(curr.copy())
                return 
            curr.append(i)
            recur(i+1, curr)
            curr.pop()
            recur(i+1, curr)
        recur(1, [])
        return res    
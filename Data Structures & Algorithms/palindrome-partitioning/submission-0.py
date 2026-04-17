class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_pali(sub):
            return sub == sub[::-1]

        def recur(j, i, cur):
            if i == len(s):
                if j == i:            
                    res.append(cur.copy())
                return

            if is_pali(s[j:i+1]):
                cur.append(s[j:i+1])
                recur(i + 1, i + 1, cur)   
                cur.pop()

            recur(j, i + 1, cur)

        recur(0, 0, [])
        return res

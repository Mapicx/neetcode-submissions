class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        worddict = set(wordDict)

        def backtrack(i):
            if len(s) == i:
                res.append(" ".join(curr))
                return
            
            for j in range(i, len(s)):
                w = s[i:j + 1]
                if w in worddict:
                    curr.append(w)
                    backtrack(j+1)
                    curr.pop()
        
        res = []
        curr = []
        backtrack(0)
        return res
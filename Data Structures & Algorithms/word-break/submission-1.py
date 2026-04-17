from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def recur(i):
            if i == len(s):
                return True
            for strr in wordDict:
                if (
                    (i + len(strr)) <= len(s) and 
                    strr == s[i : i + len(strr)]
                    ):
                    if recur(i + len(strr)):
                        return True
            return False

        return recur(0)
        
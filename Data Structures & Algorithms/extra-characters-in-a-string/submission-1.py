from functools import lru_cache
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()

        for w in dictionary:
            trie.addWord(w)
        n = len(s)

        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 0

            res = 1 + dfs(i+1)
            curr = trie.root
            for j in range(i, n):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]

                if curr.isWord:
                    res = min(res, dfs(j+1))
            return res
        return dfs(0)

        

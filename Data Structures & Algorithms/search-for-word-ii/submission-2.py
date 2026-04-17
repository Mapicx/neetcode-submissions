class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addword(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isword = True

class Solution:
    def findWords(self, board, words):
        ROWS, COLS = len(board), len(board[0])
        path = set()
        res = set()
        root = Trie()
        for w in words:
            root.addword(w)

        def dfs(r, c, node, word):

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in path or board[r][c] not in node.children):
                return 

            path.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.isword:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            
            path.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root.root, "")

        return list(res)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recur(string, open_count, close_count):
            if close_count > open_count:
                return
            if open_count > n:
                return
            if len(string) == 2 * n:
                if close_count == open_count:
                    res.append(string)
                    return            
            string = string + "("
            recur(string, open_count + 1, close_count)
            string = string[:-1] # pop the last character
            string = string + ")"
            recur(string, open_count, close_count + 1)
            string = string[:-1]
            
        recur("", 0, 0)
        return res
        
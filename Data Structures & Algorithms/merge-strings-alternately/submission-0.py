class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        tot_str1, tot_str2 = len(word1), len(word2)
        res = str()
        min_count = min(tot_str1, tot_str2)
        for i in range(min_count):
            res += word1[i]
            res += word2[i]
        if (min_count == tot_str1 and min_count == tot_str2):
            return res
        if abs(tot_str1 - min_count) != 0:
            res += word1[min_count:]
            return res
        res += word2[min_count:]
        return res

        
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        dict_t = defaultdict(int)
        for ch in t:
            dict_t[ch] += 1
        window = defaultdict(int)
        required = len(dict_t)
        formed = 0
        l = 0
        ans = (float("inf"), None, None)
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1
            if ch in dict_t and dict_t[ch] == window[ch]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = ((r - l + 1), l, r)
                char_l = s[l]
                window[char_l] -= 1

                if char_l in dict_t and window[char_l] < dict_t[char_l]:
                    formed -= 1
                l += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charSet = set()
        max_len = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            max_len = max(max_len, right-left+1)
        return max_len
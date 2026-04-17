class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(longest_prefix):
                longest_prefix = longest_prefix[:-1]
            if not longest_prefix:
                return ""
        return longest_prefix
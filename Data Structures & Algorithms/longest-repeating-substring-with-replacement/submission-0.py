class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashmap = dict()
        res = 0

        for right in range(len(s)):
            hashmap[s[right]] = 1 + hashmap.get(s[right], 0)
            if ((right - left + 1) - (max(hashmap.values()))) > k:
                hashmap[s[left]] = hashmap[s[left]] - 1
                left += 1
            res = max(res, right - left + 1)
        return res



        
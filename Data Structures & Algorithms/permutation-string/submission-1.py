class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        len_s1 = len(s1)
        if len_s1 > len(s2):
            return False
        
        target_count = Counter(s1)
        window_count = Counter(s2[:len_s1])
        
        if window_count == target_count:
            return True
        
        for i in range(len_s1, len(s2)):
            # add new char
            window_count[s2[i]] += 1
            
            # remove old char
            old_char = s2[i - len_s1]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]
            
            # check match
            if window_count == target_count:
                return True
        
        return False

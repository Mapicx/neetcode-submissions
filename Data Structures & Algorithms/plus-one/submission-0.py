class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            # if the digit is not 9
            if digits[i] != 9:
                digits[i] += 1
                return digits
            # if the digit is 9 
            digits[i] = 0
        digits.insert(0, 1)
        return digits
        
        
class Solution:
    def replaceElements(self, num: List[int]) -> List[int]:
        return [max(num[i+1:], default=-1) for i in range(len(num))]

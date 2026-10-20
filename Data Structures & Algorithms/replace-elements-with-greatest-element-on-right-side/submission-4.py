class Solution:
    def replaceElements(self, num: List[int]) -> List[int]:
        n = len(num)
        ans = [0] * n
        rightmax = -1
        for i in range(n-1, -1, -1):
            ans[i] = rightmax
            rightmax = max(num[i], rightmax)
        return ans
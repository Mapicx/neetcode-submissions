class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def cansplit(largest):
            subarray = 0
            currsum = 0

            for n in nums:
                currsum += n
                if currsum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    currsum = n
            if subarray + 1 <= k:
                return True

        while l <= r:
            mid = (l + r) // 2

            if cansplit(mid):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res

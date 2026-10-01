class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        l, r = 1, length - 2

        while l <= r:
            m = (l+r) // 2
            left, mid, right = get(m - 1), get(m), get(m + 1)
            if left < mid < right:
                l = m + 1
            elif left > mid> right:
                r = m - 1
            else:
                break
        peak = m

        l, r = 0, peak - 1
        while l <= r:
            m = (l+r) // 2
            val = get(m)
            if val < target: 
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m

        l, r = peak, length - 1
        while l <= r:
            m = (l+r) // 2
            val = get(m)
            if val > target: 
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        return -1 
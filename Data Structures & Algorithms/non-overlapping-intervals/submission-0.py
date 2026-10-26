class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[0])
        lastend = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start < lastend:
                res += 1
                lastend = min(lastend, end)
            else:
                lastend = end
        return res

class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        arr = self.data[key]
        left, right = 0, len(arr) - 1
        res = ""  # default return if no timestamp <= given

        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]   # candidate answer
                left = mid + 1      # try to find later timestamp
            else:
                right = mid - 1

        return res

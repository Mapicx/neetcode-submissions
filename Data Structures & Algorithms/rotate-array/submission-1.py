class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # k = k % len(nums)

        # for _ in range(k):
        #     nums.insert(0, nums[-1])
        #     nums.pop()

        # Approach 2

        k %= len(nums)
        nums.reverse()

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
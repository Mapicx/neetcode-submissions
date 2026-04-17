class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output_set = set()
        j = 0
        k = len(nums) - 1
        for i in range(len(nums) - 2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))  
                    output_set.add(triplet)
                    j += 1
                    k -= 1
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1

        return [list(t) for t in output_set]                        



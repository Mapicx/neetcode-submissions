class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        list_run = []
        output_list = []

        for i in range(0, len(nums)):

            for j in range(i + 1, len(nums)):

                for k in range(j + 1, len(nums)):
                    
                        if nums[i] + nums[j] + nums[k] == 0:
                            list_run.append(nums[i])
                            list_run.append(nums[j])
                            list_run.append(nums[k])
                            output_list.append(list_run)
                            list_run = []
                        k += 1
                
                j += 1
            
            i += 1
        
        lst = [sorted(sublist) for sublist in output_list]
        unique = list(set(tuple(sublist) for sublist in lst))
        result = [list(t) for t in unique]
        return result



        
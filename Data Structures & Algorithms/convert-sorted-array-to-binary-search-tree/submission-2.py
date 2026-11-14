class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])

            root.left = dfs(nums[:mid])
            root.right = dfs(nums[mid+1:])

            return root
        return dfs(nums)
        


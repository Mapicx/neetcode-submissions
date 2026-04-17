# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.good_count = 0

    def goodNodes(self, root: TreeNode) -> int:
        def findgoodnodes(root, max_seen = 0) -> int:
            if not root:
                return 0
            
            if root.val >= max_seen:
                self.good_count += 1
            findgoodnodes(root.left, max(max_seen, root.val))
            findgoodnodes(root.right, max(max_seen, root.val))
            return self.good_count

        return findgoodnodes(root, root.val)
            




        


        
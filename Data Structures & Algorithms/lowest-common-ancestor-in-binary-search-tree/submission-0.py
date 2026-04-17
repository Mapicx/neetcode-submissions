# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Traverse the tree
        while root:
            # If both p and q are smaller than root, LCA is in the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both p and q are greater than root, LCA is in the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                # We have found the split point
                return root
        return None

            

            

        
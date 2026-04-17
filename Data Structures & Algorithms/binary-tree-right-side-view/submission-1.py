# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        lst = []

        while queue:
            lenqueue = len(queue)
            rightmost = None

            for i in range(lenqueue):
                node = queue.popleft()
                rightmost = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lst.append(rightmost.val)
        return lst
                
        
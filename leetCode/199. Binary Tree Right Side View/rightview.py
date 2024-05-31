# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        rightSide = []
        queue = deque([root])

        while queue:
            nodesNumberOnLevel = len(queue)

            for i in range(nodesNumberOnLevel):

                node = queue.popleft()

                if i == nodesNumberOnLevel - 1:
                    rightSide.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return rightSide
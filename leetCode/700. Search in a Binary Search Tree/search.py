# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def searchNode(self, root: Optional[TreeNode], val: int) -> TreeNode:
        
        current_node = root
        while current_node is not None:
            if val == current_node.val:
                return current_node
            elif val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None
                
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        target_node = self.searchNode(root, val)

        if target_node is None:
            return None
        
        return target_node
        
        # tree_nodes_list = []

        # queue =  deque([target_node])

        # while queue:
            
        #     nodesNumberOnLevel = len(queue)

        #     for i in range(nodesNumberOnLevel):
                
        #         node = queue.popleft()

        #         tree_nodes_list.append(node.val)

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return tree_nodes_list
        
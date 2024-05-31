from rightview import TreeNode, Solution


sol = Solution()

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode (3)

assert sol.rightSideView(root) == [0, 2, 3]
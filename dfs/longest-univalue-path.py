"""
Given the root of the binary tree, find the longest path where all nodes along the path have the same value. This path doesn't have to include the root node. Return the number of edges on that path, not the number of nodes.
"""

from dfs import TreeNode


def longestUnivaluePath(root):
    max_length = 0

    def dfs(node):
        nonlocal max_length
        if not node:
            return 0

        left_length = dfs(node.left)
        right_length = dfs(node.right)

        left_arrow = right_arrow = 0

        # check if children have the same value as the current node,
        # which means we can extend the univalue path by including the
        # current node
        if node.left and node.left.val == node.val:
            left_arrow = left_length + 1
        if node.right and node.right.val == node.val:
            right_arrow = right_length + 1

        # left_arrow + right_arrow is the length of the longest
        # univalue path that goes through the current node
        max_length = max(max_length, left_arrow + right_arrow)
        return max(left_arrow, right_arrow)

    dfs(root)
    return max_length


print(
    longestUnivaluePath(
        TreeNode(
            1,
            TreeNode(1, TreeNode(1), TreeNode(1)),
            TreeNode(1, TreeNode(1), TreeNode(1)),
        )
    )
)

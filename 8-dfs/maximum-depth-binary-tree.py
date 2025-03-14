"""
Given the root of a binary tree, write a recursive function to find its maximum depth, where maximum depth is defined as the number of nodes along the longest path from the root node down to a leaf node.

"""

from typing import Optional

from dfs import TreeNode


def maxDepth(node: Optional[TreeNode]) -> int:
    # for each subtree, i need to know the depth of the subtree, so each recursive call needs to return the max depth of the subtree
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    left = maxDepth(node.left)
    right = maxDepth(node.right)
    return max(left, right) + 1


print(
    # [4, 2, 7, 1, null, 6, 9, null, 8, null, null, null, null, null, null]
    maxDepth(
        TreeNode(
            4,
            TreeNode(2, TreeNode(7), TreeNode(1)),
            TreeNode(
                6,
                TreeNode(9),
                TreeNode(
                    8,
                    TreeNode(9),
                    TreeNode(9),
                ),
            ),
        )
    )
)

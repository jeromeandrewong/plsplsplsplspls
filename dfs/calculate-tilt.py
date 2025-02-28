"""
Given the root node of a binary tree, write a recursive function to return the sum of each node's tilt.

The tilt of a node is the absolute difference between the sum of its left subtree and the sum of its right subtree. If a node has an empty left or subtree, the sum of the empty subtree is 0.
"""

from typing import Optional

from dfs import TreeNode


def calculateTilt(root: Optional[TreeNode]) -> int:
    tilt = 0

    def dfs(node) -> int:
        nonlocal tilt
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        tilt += abs(left - right)
        # return the sum of current subtree
        return left + right + node.val

    dfs(root)

    return tilt


print(
    calculateTilt(
        TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        )
    )
)

"""
complexity is O(n) because we visit each node once and we do constant time work each time.
"""

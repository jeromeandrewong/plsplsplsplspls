"""
Given the root of a binary tree, write a recursive function to find the diameter of the tree. The diameter of a binary tree is the length of the longest path (# of edges) between any two nodes in a tree. This path may or may not pass through the root.
"""

from typing import Optional
from dfs import TreeNode

"""
1. return values: max depth of each subtree
2. base case: empty tree/leaf node
3. global variable: current max depth of entire tree
4. helper function: dont need but bec we need global, good to define within maxDiameter
"""


def maxDiameter(root: Optional[TreeNode]) -> int:
    max_ = 0

    def dfs(root) -> int:
        nonlocal max_

        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)

        max_ = max(max_, left + right)

        return 1 + max(left, right)

    dfs(root)

    return max_


print(
    maxDiameter(
        TreeNode(
            3,
            TreeNode(9, TreeNode(1, TreeNode(2)), TreeNode(3, TreeNode(4))),
        )
    )
)

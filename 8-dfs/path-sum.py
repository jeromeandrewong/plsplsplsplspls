"""
Given the root of a binary tree and an integer target, write a recursive function to determine if the tree has a root-to-leaf path where all the values along that path sum to the target.

EXPLANATIN:
If im a node in a tree, what do i need from my left and right subtrees to solve the problem for my subtree?
in order for there to ba a path from root to leaf that sums to a target, there must be a path from either left or right child that sums to `targer - node.val`
"""

from typing import Optional

from dfs import TreeNode


def has_path_sum(node: Optional[TreeNode], target: int) -> bool:

    if node is None:
        return False

    # at leaf node, check if target == value
    if not node.left and not node.right:
        return node.val == target

    target -= node.val

    left = has_path_sum(node.left, target)
    right = has_path_sum(node.right, target)

    return left or right


# [4, 2, 7, 1, 3, 6, 9], target=17
print(
    "TEST CASE 1:",
    has_path_sum(
        TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        ),
        17,
    ),
)
# [4, 2, 7, 1, 3, 6, 9] target = 13
print(
    "TEST CASE 2:",
    has_path_sum(
        TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        ),
        13,
    ),
)

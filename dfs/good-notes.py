"""
Passing Values Down and Helper Functions:

Previously we solved BT problems using a bottom up approach, but in some cases, we would need to pass information "down" from parents to child nodes, and can be done through parameters of a recursive function. If we need more parameters than our original function signature allows, we need out own helper function

Questions involving root to leaf paths are common examples of where using helper functions are necessary to introduce extra parameters that store the state of the current path

DESCRIPTION:
Given the root node of a binary tree, write a function to find the number of "good nodes" in the tree. A node X in the tree is considered "good" if in the path from the root to the node X, there are no nodes with a value greater than X's value.
"""

from typing import Optional

from dfs import TreeNode


def goodNodes(root: Optional[TreeNode]) -> int:
    def dfs(root, max_) -> int:
        if root is None:
            return 0

        count = 0
        if root.val >= max_:
            count += 1
            max_ = root.val

        left = dfs(root.left, max_)
        right = dfs(root.right, max_)
        return left + right + count

    return dfs(root, -float("inf"))


"""
Global Variables:
sometimes using global variables that recursive calls can access can simplify code
"""


def goodNodes2(root: Optional[TreeNode]) -> list[TreeNode]:
    nodes = []

    def dfs(root, max_):
        nonlocal nodes
        if root is None:
            return

        if root.val >= max_:
            max_ = root.val
            nodes.append(root)

        dfs(root.left, max_)
        dfs(root.right, max_)

    dfs(root, -float("inf"))
    return nodes

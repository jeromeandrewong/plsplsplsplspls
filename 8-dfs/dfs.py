"""
When solving a binary tree problem with recursion, the first step is to figure out the return value of each recursive call. In the problem above, each recursive call returned the sum of the subtree rooted at the current node.
To determine what the return value should be for a different problem, imagine you're at a node in the tree and ask yourself: "What information do I need from my left and right subtrees to solve the problem for my subtree?"

Common Mistakes:

1. Returns Value
- Not being able to clearly define what each recursive call returns in terms of the node it is called on. This leads to incorrect return values, particulary in the base cases.

2. Base Cases
- Make sure that the return value of the base case and the return value of the recursive case are of the same type. A common mistake is to return None for the base case and an integer in the recursive case.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_sum(node: Optional[TreeNode]) -> int:
    # empty tree
    if node is None:
        return 0

    # leaf node
    if node.left is None and node.right is None:
        return node.val

    leftSum = count_sum(node.left)
    rightSum = count_sum(node.right)

    return leftSum + rightSum + node.val


# print(
#     count_sum(
#         TreeNode(
#             1,
#             TreeNode(2, TreeNode(3), TreeNode(4)),
#             TreeNode(5, TreeNode(6), TreeNode(7)),
#         )
#     )
# )


def find_max(node: Optional[TreeNode]) -> int:
    # empty tree
    if node is None:
        return int("-inf")

    # leaf node
    if node.left is None and node.right is None:
        return node.val

    left = find_max(node.left)
    right = find_max(node.right)

    return max(node.val, left, right)


"""
Passing Values Down and Helper Functions:

Previously we solved BT problems using a bottom up approach, but in some cases, we would need to pass information "down" from parents to child nodes, and can be done through parameters of a recursive function. If we need more parameters than our original function signature allows, we need out own helper function

Questions involving root to leaf paths are common examples of where using helper functions are necessary to introduce extra parameters that store the state of the current path

DESCRIPTION:
Given the root node of a binary tree, write a function to find the number of "good nodes" in the tree. A node X in the tree is considered "good" if in the path from the root to the node X, there are no nodes with a value greater than X's value.
"""


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

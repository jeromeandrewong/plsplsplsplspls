"""
Given the root of a binary, write a recursive function to determine if it is a valid binary search tree.

A tree is a BST if the following conditions are met:

1. Every node on the left subtree has a value less than the value of the current node.

2. Every node on the right subtree has a value greater than the value of the current node.

3. The left and right subtrees must also be valid BSTs.
"""

from typing import Optional

from dfs import TreeNode


def isValidBST(node: Optional[TreeNode]) -> bool:

    # to validate BST, every node needs to be in a valid range(bigger than left, smaller than right)
    # since we need more parameters to pass down, we can use a helper function
    def dfs(node, min_, max_):
        if node is None:
            return True

        if node.val <= min_ or node.val >= max_:
            return False

        return dfs(node.left, min_, node.val) and dfs(node.right, node.val, max_)

    return dfs(node, -float("inf"), float("inf"))


print(isValidBST(TreeNode(2, TreeNode(1), TreeNode(4))))
print(isValidBST(TreeNode(4, TreeNode(1), TreeNode(5, TreeNode(3), TreeNode(6)))))

"""
Return Values:
If I'm at a node in the tree, what values do I need from my left and right children to tell if the current subtree is a valid binary search tree?
The current subtree is a valid binary search tree if:
- The left subtree is a valid binary search tree.
- The right subtree is a valid binary search tree.
- And the value of the current node falls within the valid range.
This tells me that each recursive call should return a boolean value indicating whether the current subtree is a valid binary search tree.

Base Case:
An empty tree is a valid binary search tree.

Extra Work:
The work that we need to do at each node is to check if the current node's value falls within the valid range. If it doesn't we can return False immediately.

Helper Functions:
Since we need to pass the minimum and maximum values down to their children, we need to introduce a helper function to keep track of these values.
This helper function will introduce two parameters, min_ and max_, which represent the range of values that the current subtree's nodes can take on. The helper function will return a boolean value indicating whether the current subtree is a valid binary search tree.
When we recurse to our left child, we:
Pass the current node's value as the new max_ value, since the left child's value must be less than the current node's value. min_ remains the same.
When we recurse to our right child, we:
Pass the current node's value as the new min_ value, since the right child's value must be greater than the current node's value. max_ remains the same.
"""

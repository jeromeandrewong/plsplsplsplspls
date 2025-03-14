"""
Given the root of a binary tree and an integer target, write a recursive function to find all root-to-leaf paths where the sum of all the values along the path sum to target.
"""

"""
return values: dont need return values in recursive calls, just need maintain state of current path
base case: empty tree/leaf node
global variable: all possible paths
helper function: need to pass down remaining target sum and values along current path
"""


from dfs import TreeNode


def path_sum2(root, target):
    result = []

    def dfs(root, target, path):
        if not root:
            return

        path.append(root.val)
        if not root.left and not root.right:
            if root.val == target:
                result.append(path[:])

        dfs(root.left, target - root.val, path)
        dfs(root.right, target - root.val, path)

        path.pop()

    dfs(root, target, [])
    return result


print(
    path_sum2(
        TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(7)),
            TreeNode(4, TreeNode(5), TreeNode(1)),
        ),
        10,
    )
)

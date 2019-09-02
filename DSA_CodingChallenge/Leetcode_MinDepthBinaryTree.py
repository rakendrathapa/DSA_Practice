"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        print('root:{}'.format(root.val))
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        depth = 1
        if root.right and root.left:
            depth += min(self.minDepth(root.right), self.minDepth(root.left))
        elif root.right:
            depth += self.minDepth(root.right)
        else:
            depth += self.minDepth(root.left)
        print('root:{} depth:{}'.format(root.val, depth))
        return depth


def stringToTreeNode(inputValues):
    if not inputValues:
        return None

    root = TreeNode(inputValues[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item is not None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item is not None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def testmain():
    testcases = list()
    testcases.append([3, 9, 20, None, None, 15, 7])

    sol = Solution()
    for cases in testcases:
        root = stringToTreeNode(cases)
        print('depth =', sol.minDepth(root))

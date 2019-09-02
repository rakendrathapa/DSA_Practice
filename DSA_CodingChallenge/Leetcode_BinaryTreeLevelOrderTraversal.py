"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        leveldict = defaultdict(list)
        q = deque()
        q.appendleft((root, 0))
        while len(q) != 0:
            item = q.pop()
            # print('item:{}'.format(item))
            node, level = item
            leveldict[level].append(node.val)
            if node.left is not None:
                q.appendleft((node.left, level + 1))
            if node.right is not None:
                q.appendleft((node.right, level + 1))

        levellist = list()
        for level in leveldict:
            # print(level)
            levellist.append(leveldict[level])

        return levellist

    def stringToTreeNode(self, inputValues):
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
    testcase = list()
    testcase.append([3, 9, 20, None, None, 15, 7])

    sol = Solution()
    for case in testcase:
        root = sol.stringToTreeNode(case)
        print(sol.levelOrder(root))


if __name__ == '__main__':
    testmain()

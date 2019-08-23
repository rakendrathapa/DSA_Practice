import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBSTUtil(self, node, leftmin, rightmax):
        if node is None:
            return True
        if node.val < leftmin or node.val > rightmax:
            return False
        return self.isValidBSTUtil(node.left, leftmin, node.val - 1) and self.isValidBSTUtil(node.right, node.val + 1, rightmax)

    def isValidBST(self, root):
        leftmin = -sys.maxsize - 1
        rightmax = sys.maxsize
        print('leftmin:{} rightmax:{}'.format(leftmin, rightmax))
        return self.isValidBSTUtil(root, leftmin, rightmax)

def main():
    root = TreeNode(2)
    root.left=1
    root.right=3
    sol = Solution().isValidBST(root)

if __name__ == '__main__':
    main()

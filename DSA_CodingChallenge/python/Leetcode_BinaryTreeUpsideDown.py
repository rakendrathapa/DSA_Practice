"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling
(a left node that shares the same parent node) or empty, flip it upside down and
turn it into a tree where the original right nodes turned into left leaf nodes.
Return the new root.
Example:
Input: [1,2,3,4,5]
    1
   / \
  2   3
 / \
4   5
Output: return the root of the binary tree [4,5,2,#,#,3,1]
    4
  / \
 5   2
    / \
   3   1
Clarification:
Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is serialized on OJ.
The serialization of a binary tree follows a level order traversal, where '#' signifies a
path terminator where no node exists below.
Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        if root is None or root.left is None:
            return root

        parent = None
        curr_node = root
        new_node = None
        last_right = None

        while curr_node is not None:
            new_node = curr_node.left
            curr_node.left = last_right
            last_right = curr_node.right
            curr_node.right = parent
            parent = curr_node
            curr_node = new_node
        return parent

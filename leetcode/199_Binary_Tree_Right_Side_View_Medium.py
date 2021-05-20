'''
199. Binary Tree Right Side View Medium
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.view = []
        self.recursive(root, 0)
        return self.view
    
    def recursive(self, node: TreeNode, height) -> List[int]:
        if node: 
            if height == len(self.view):
                self.view.append(node.val)

            self.recursive(node.right, height+1)
            self.recursive(node.left, height+1)
            

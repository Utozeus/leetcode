# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        else :
            return self.isBalanced(root.left) and self.isBalanced(root.right) and (abs(self.heightFind(root.left)-self.heightFind(root.right))<=1) 
            
            
#             root.left=None and root.right=None :
#             return True
#         if root.left=None and root.right=None :
#             return 0
#         elif root.left=None and root.right!=None:
#             return 1+self.heightFind(root.right)
#         elif root.left!=None and root.right=None:
#             return 1+self.heightFind(root.left)
#         else :
#             return 1+max(self.heightFind(root.left), self.heightFind(root.right))

    @classmethod
    def heightFind(self, root):
        if root==None:
            return 0
#         elif root.left=None and root.right=None :
#             return 0
#         elif root.left=None and root.right!=None:
#             return 1+self.heightFind(root.right)
#         elif root.left!=None and root.right=None:
#             return 1+self.heightFind(root.left)
        else :
            return 1+max(self.heightFind(root.left), self.heightFind(root.right))
        
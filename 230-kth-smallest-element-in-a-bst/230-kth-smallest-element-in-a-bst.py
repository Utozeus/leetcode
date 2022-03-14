# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root==None:
            return None
        
        
        visitList=[] #for in-order stack
                
        return self.help(root, visitList)[k-1]
        
        
    @classmethod    
    def visit(self, root, visitList):
        if root==None:
            return visitList
        else :
            return visitList+[root.val]
    
    @classmethod
    def help(self, root, visitList) :
        if root==None:
            return visitList
        else :
            if root.left!=None:
                visitList=self.help(root.left, visitList)
                visitList=self.visit(root,visitList)
                visitList=self.help(root.right, visitList)
                return visitList
            else : #root.left==None
                visitList=self.visit(root, visitList)
                visitList=self.help(root.right, visitList)
                return visitList
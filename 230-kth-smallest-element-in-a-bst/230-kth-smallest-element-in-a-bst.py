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
                
        return self.help(root, visitList,k)[k-1]
        
        
    @classmethod    
    def visit(self, root, visitList):
        if root==None:
            return visitList
        else :
            return visitList+[root.val]
    
    @classmethod
    def help(self, root, visitList, k) :
        
        if root==None:
            return visitList
        else :
            if root.left!=None:
                if len(visitList)==k:
                    return visitList
                else:
                    visitList=self.help(root.left, visitList,k)
                    visitList=self.visit(root,visitList)
                    visitList=self.help(root.right, visitList,k)
                    return visitList
            else : #root.left==None
                if len(visitList)==k:
                    return visitList
                else:
                    visitList=self.visit(root, visitList)
                    visitList=self.help(root.right, visitList,k)
                    return visitList
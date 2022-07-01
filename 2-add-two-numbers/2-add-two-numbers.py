# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        answer=ListNode()
        ans_temp=answer
        # ans_temp=ListNode()
        l1_temp=l1
        l2_temp=l2
        roundup=0
        num=0
        
        while (l1_temp!=None or l2_temp!=None or roundup!=0) :
            
            if num!=0 :
                ans_temp.next = ListNode()
                ans_temp=ans_temp.next
            num+=1
            
            temp=0
            
            if l1_temp!=None:
                temp+=l1_temp.val
            if l2_temp!=None:
                temp+=l2_temp.val
            if roundup!=0:
                temp+=roundup
                                   
            if temp >= 10 :
                roundup = 1
                temp = temp-10
            else :
                roundup = 0
                
            ans_temp.val=temp
            
            #update
            if l1_temp!=None :
                l1_temp=l1_temp.next
            if l2_temp!=None :
                l2_temp=l2_temp.next
            
        return answer
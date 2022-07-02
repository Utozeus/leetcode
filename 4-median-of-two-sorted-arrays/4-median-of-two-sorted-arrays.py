class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        n=len(nums1)
        m=len(nums2)
        
#         if num1[0] >= num2[-1] :
#             return
#         elif num2[0] >= num1[-1] :
#             return
#         elif 
        
        if (n+m) == 0 :
            return None
        
        temp=[0] * (n+m)
        temp[:n]=nums1
        temp[n:]=nums2
        temp.sort()
        
        if (n+m)%2==1 :
            return temp[(n+m)//2]
        else :
            return ( temp[(n+m)//2-1] + temp[(n+m)//2] )/float(2)
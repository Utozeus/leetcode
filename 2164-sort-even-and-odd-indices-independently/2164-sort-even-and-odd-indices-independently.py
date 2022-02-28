class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #odd indices ordering change by insertion sort
        
        for i in range(3,len(nums),2):
            loc=i
            while ((loc>1) and (nums[loc]>=nums[loc-2])) :
                nums[loc], nums[loc-2]=nums[loc-2], nums[loc]
                loc-=2
                
        #even indices ordering change by insertion sort
        
        for i in range(2,len(nums),2):
            loc=i
            while ((loc>0) and (nums[loc]<=nums[loc-2])) :
                nums[loc], nums[loc-2]=nums[loc-2], nums[loc]
                loc-=2
        return nums
        


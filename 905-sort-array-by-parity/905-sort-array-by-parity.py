class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        if n>1:
            i=-1
            for j in range(n):
                if nums[j]%2==0 :
                    i+=1
                    nums[i], nums[j] =nums[j], nums[i]
        return nums
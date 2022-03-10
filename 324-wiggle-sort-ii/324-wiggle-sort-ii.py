class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        nums.sort(reverse=True)
        even=nums[:len(nums)//2]
        odd=nums[len(nums)//2:]
        nums[1::2]=even
        nums[::2]=odd

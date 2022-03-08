class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        temp=[]
        for i, num in enumerate(nums):
            temp.append([int(num), i])
        temp.sort()
        return nums[temp[-k][1]]
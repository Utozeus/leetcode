class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #point dictionary 생성
        maxVal=max(nums)
        point=dict(zip(range(1,maxVal+1),[0]*maxVal))
        for num in nums:
            point[num]+=num
        
        ans=[0]*(maxVal+1) #ans 담을 변수
        ans[1]=point[1]
        
        for i in range(2, maxVal+1) :
            ans[i]=max(ans[i-2]+point[i], ans[i-1])
        return ans[maxVal]
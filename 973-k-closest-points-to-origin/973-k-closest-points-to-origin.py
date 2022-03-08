class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        lengthList=[]
        for x,y in points:
            lengthList.append((x**2+y**2))
        
        temp=sorted(zip(lengthList, points))
        
        sol=[]
        for i in range(k) :
            sol.append(temp[i][1])
        return sol
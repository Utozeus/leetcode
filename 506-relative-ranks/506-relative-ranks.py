class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        #ordering scores       

        temp=[] #for matching btwn 'score' and 'rank' // 
        for num in score:
            temp.append(num)
        #주의 ★★★★ list 변수를 temp로 만들 때는 그냥 같다고 하면,,temp를 변경하는 행위가 본래 list를 변경하는 결과를 초래

        self.quickSort(temp, 0, len(temp)-1) #reordering in descending order
#         print("temp after sorting is", temp)
#         print("score after sorting is", score)


        #matching btwn 'score' and 'rank'
        matDic=dict() #matching dictionary
        for i, num in enumerate(temp) :
            matDic[num]=i+1 #key is 'score' and value is 'rank'
#         print("matDic is", matDic)        


        #building rank
        rank=[]
        for num in score:
            rank.append(matDic[num])
#             print("num is", num, "and rank is", rank)
#         print("rank is", rank)        
        
        #building result
        result=[]
        for num in rank:
            if num==1:
                result.append("Gold Medal")
            elif num==2:
                result.append("Silver Medal")
            elif num==3:
                result.append("Bronze Medal")
            else:
                result.append(str(num))
#         print("result is", result)        
        return result

    
#     @classmethod
    def quickSort(self, A , p, r ) :
        if p<r :
            q = self.partition(A, p, r)
            self.quickSort(A, p, q-1)
            self.quickSort(A, q+1, r)
        else :
            return
        
#     @classmethod
    def partition(self, A , p, r)  :
        base=A[r]
        i=p-1
        for j in range(p,r) :
            if A[j]>=base :
                i+=1
                A[i], A[j]=A[j], A[i]
        q=i+1
        A[q],A[r]=A[r], A[q]
        return q

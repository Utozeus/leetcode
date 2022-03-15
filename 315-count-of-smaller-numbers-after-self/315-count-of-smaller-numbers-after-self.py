class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #mergeSort를 하면서, 각 원소별로 자신의 왼쪽으로 넘어가는 원소의 개수를 record하여 return
        numWithId = [ (num, i) for i, num in enumerate(nums) ]
        result = [0]*len(nums)
        sortedList, result = self.mergeSort(numWithId,0,len(nums),result)
        return result
    
#     <main idea>
#     nums를 mergeSort(in Descending Order)하면서, 
#     각 원소별로  
#     기존에 해당 원소의 우측에 있던 원소가 
#     왼쪽으로 이동하는 경우
#     해당 건수를 기록할 예정
    
#     <방법>
#     nums list 각 element의 index 정보를 이용하여야 하므로,
#     index를 tuple로 추가한 새로운 list를 만든 뒤
#      *  numWithId = [ (num, i) for i, num in enumerate(nums) ]

#     해당 list를 mergeSort하면서,
#     count할 정보를 기록할 list를 별도로 만들어 기록
#     result = [0]*len(nums)
    @classmethod    
    def mergeSort(self, A, p, q, res) :
    # the end of recursion
        if q-p==1 :# when length is 1 -> return itself
            return A[p:q], res
    
        else :
            # divide list
            r=p+(q-p)//2

            # for each list call mergeSort
            left, res = self.mergeSort(A, p, r, res)
            right, res = self.mergeSort(A, r, q, res)

            # merge that two lists
            id_left=0
            id_right=0
            i=0
            while ( (id_left<r-p) and (id_right<q-r) ) :
                if left[id_left][0]>right[id_right][0] :
                    A[p+i]=left[id_left]
                    res[left[id_left][1]]+=len(right)-id_right
                    id_left+=1
                else :
                    A[p+i]=right[id_right]
                    id_right+=1
                i+=1
            if id_left==r-p :
                A[p+i:q]=right[id_right:q-r]
            elif id_right==q-r :
                A[p+i:q]=left[id_left:r-p]

            return A[p:q], res


        
        
        
        #Second Trial->Time Exceed        
#         answer=[0]*len(nums)
#         for i in range(len(nums)-1):
#             answer[i]=sum([nums[j] < nums[i] for j in range(i+1,len(nums))])
#         return answer    
        
        
        
        #First Trial -> Time Exceed
        
        # answer=[0]*len(nums)
        # for i in range(len(nums)-1) :
        #     temp=nums[i]
        #     count=0
        #     for j in range(i+1, len(nums)):
        #         if nums[j]<temp:
        #             count+=1
        #     answer[i]=count
        # return answer
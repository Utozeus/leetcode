class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
##################################################################        
#         #by using embedded ftn in python
        nums.sort()
        return nums[-k]
##################################################################


# ##################################################################       
#     #by using Quick Sort algorithm logic
#         return self.selectQuick(nums,0,len(nums)-1,k)
# ##################################################################         
#     ## following is Quick Sort algorithm logic
    
#     @classmethod
#     def selectQuick(self, A, p, r, k): 

#         if p==r :
#             if k==1 :
#                 return A[p]
#             else :
#                 return 99999
#         else :
#             q=self.partition(A,p,r)
#             #A[r] 값을 기준으로 
#             #왼쪽에는 해당 값보다 작은 element, 
#             #오른족에는 큰 element가 배열되며, 
#             #A[r]값의 새로운 위치(q)가 return


#             if (r-q)==(k-1) :
#                 return A[q]

#             else :
#                 if (r-q) < (k-1) : #q 좌측에서 찾아야 함
#                     return self.selectQuick(A,p,q-1,k-(r-q+1))
#                 else : # r-q > k-1 #q 우측에서 찾아야 함
#                     return self.selectQuick(A,q+1,r,k)
        
#     @classmethod
#     def partition(self, A, p, r):

#         if p==r :
#             return p
        
        
#         pivot=A[r]
#         i=p-1
#         for j in range(p,r) :
#             if A[j]<=pivot :
#                 i+=1
#                 A[i], A[j]=A[j], A[i]
#         q=i+1
#         A[q], A[r]=A[r], A[q]
        
#         return q
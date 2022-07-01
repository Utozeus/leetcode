class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        '''
        version 1
        '''
#         n=len(s)
        
#         ans=0 #maximum length
        
#         for i in range(n) :
            
#             start=i
#             end=i
#             tempset={s[i]}
            
#             same=False
#             while same is False :
#                 templen_before=len(tempset) #reference
#                 end=min(end+1, n-1) #increment 1 with upperbound
#                 tempset.add(s[end])
#                 templen_after=len(tempset) #reference
#                 same=(templen_before==templen_after)
#                 if ans < len(tempset) :
#                     ans = len(tempset)
            
#         return ans

        '''
        version 2
        '''
        
        temp_dict={}
        start=0
        maxlen=0
        
        for i, c in enumerate(s) :
            
            if ( ( c in temp_dict ) and ( start <= temp_dict[c] ) ) :
                start=temp_dict[c]+1
            else :
                maxlen=max(maxlen, i-start+1)
            
            
            temp_dict[c]=i
        
        return maxlen
            
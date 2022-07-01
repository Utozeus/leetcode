class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        
        ans=0 #maximum length
        
        for i in range(n) :
            
            start=i
            end=i
            tempset={s[i]}
            
            same=False
            while same is False :
                templen_before=len(tempset) #reference
                end=min(end+1, n-1) #increment 1 with upperbound
                tempset.add(s[end])
                templen_after=len(tempset) #reference
                same=(templen_before==templen_after)
                if ans < len(tempset) :
                    ans = len(tempset)
            
        return ans
                
                
            
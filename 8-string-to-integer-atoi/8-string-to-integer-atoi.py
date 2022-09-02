class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ans=0
        sign=1
        
        if len(s) ==0 :
            return ans
        
        s_idx=0 #starting index
        while ( s_idx < len(s)-1 ) and ( s[s_idx]==' ' ) :
            s_idx+=1

        if s[s_idx] == ' ' :
            return ans

        if s[s_idx]=='+' or s[s_idx]=='-' :
            sign=2*(s[s_idx]=='+')-1
            s_idx+=1

        while s_idx<len(s) and s[s_idx].isnumeric() :
            if sign==(-1) and float(s[s_idx])/10 > 214748364.8 - float(ans) :
                return -2147483648
            elif sign==1 and float(s[s_idx])/10 > 214748364.7 - float(ans) :
                return 2147483647
            else :
                ans=10*ans+int(s[s_idx])
                s_idx+=1

        return ans*sign
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ans=""
        for i in range(len(s)) :
            tmp=self.helper(s, i, i)
            if len(tmp) > len(ans) :
                ans=tmp
            
            if i+1<len(s) and s[i]==s[i+1] :
                tmp=self.helper(s, i, i+1) 
                if len(tmp) > len(ans) :
                    ans=tmp
        return ans
        
    def helper(self, s, l, r) :
        while l>=0 and r<len(s) and s[l]==s[r] :
            l-=1
            r+=1
        return s[l+1 : r]

#2차시도 time limit 초과로 실패        
#         inv_s=s[::-1]
#         L=len(s)
        
#         for j in range(L, 0, -1) :  #길이가 j인 대칭어가 있는지 살피며,
#             for i in range(L+1-j) :  #시작점의 index는 i 가 됨
#                 # candidate=s[i : i+j]
#                 # if candidate==candidate[::-1] :
#                 #     return candidate
#                 if s[i : i+j] == inv_s[L-(i+j) : L-i] :
#                     return s[i : i+j] 
                
#불필요한 search를 줄이는 logic 필요                
                
    
        
        
        
#1차시도 문제 오해석으로 실패        
        #아래 내용이 아니었음....ㅠㅠ 삽질.... 대칭인 가장 긴 단어를 찾는 것임,,
        #수미상관인 최대길이의 단어
        #길이를 measure 하는 변수가 필요 (length)
        #같은 문자가 등장한 적이 있었는지를 파악하여야 함(string별로 최초등장 최종등장 위치 정보를 기록 list 길이 3)
        #가장 긴 문자를 찾는 것이므로, 첫번째 등장 이후의 위치 정보는 업데이트 하는 방식으로 처리
        #dictionary 업데이트 하면서 최대 길이 찾기(max_length)
#         s_dict={}
#         max_len=0 #최대 길이 기록
#         max_char=s[0] #최대 길이를 가지는 character 기록 
        
#         for i, c in enumerate(s) :
            
#             if c not in s_dict : #최초 등장 단어 dictionary 등록
#                 s_dict[c]=[i, i] #value는 최초등장 위치 및 최종등장 위치
                
#             else : # if c in s_dict : #최종등장 업데이트
#                 temp=s_dict[c]
#                 temp[1]=i #최종등장 위치 업데이트
#                 s_dict[c]=temp #최종등장 위치 업데이트
                
#                 #최종길이 확인 후 max length를 가지는 character fix
#                 if max_len < (temp[1] - temp[0] + 1 ) : #만약 해당 단어의 길이가 여태까지 단어 중 가장 긴 것이라면
#                     max_len = temp[1] - temp[0] + 1 #max_len 을 업데이트하고
#                     max_char = c #해당 character를 기록
                    
                    
#         return s[s_dict[max_char][0] : s_dict[max_char][1]+1]
                
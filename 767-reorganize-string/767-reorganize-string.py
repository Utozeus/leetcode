class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        counter=Counter(s)
        picked=None 
        ans='_' # _ is sentinel
        
        while counter :
            
            #가장 많은 2개의 문자 중, 직전에 입력한 것과 다른 문자를 선택
            for ele, num in counter.most_common(2):
                if ele!=ans[-1] : 
                    picked=ele
                    break
            # print(f"counter.most_common(2) is ★{counter.most_common(2)}")
            # print(f"picked is ★{picked}")
            # 선택한 문자를 추가
            if picked!=None:
                ans+=picked
                # print(f"updated ans is ★{ans}")
                # 사용후 사용내역을 반영
                counter[picked]-=1 #사용 후 개수 제거
                if counter[picked]<=0 :
                    counter.pop(picked)
                # print(f"after adding, counter is ★{counter}")
                #picked 업데이트
                picked=None
            else : #pick이 안 되면 끝냄
                break

        ans=ans[1:]
        if len(ans)==len(s) :
            return ans
        else :
            return ""
                
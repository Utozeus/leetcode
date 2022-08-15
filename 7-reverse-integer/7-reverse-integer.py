class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 절대값을 2^31-1 이하로 bound 시키기
        if x==-2147483648 :
            return 0

        # 양수로 만들어 다룰 예정(variable "tmp")
        tmp=x
        negative=(x<0) #음수면 true
        if negative :
            tmp=-tmp

        
        # 10진법으로 표현했을 때의 각 자리수를 list에 기록
        coeff=[0]*10 #자리수별 값을 담을 list
        for i in range(10, 0 , -1) :
            y=tmp//10**(i-1)
            coeff[i-1]=y
            tmp-=y*10**(i-1)
        
        # 원래 x에서 최초로 0이 아닌 자리수(j) 찾기
        j=9
        while j > 0 and coeff[j]==0 :
            j-=1

        
        t=0 # ans 만들 때 사용할 변수(10의 t승)

        #답을 담을 변수 선언
        ans=0
        
        for i in range(j, -1, -1) :
            
            # 역으로 표현했을 때 range를 벗어나버리면 0이 되도록 선언
            if ( i==0 ) and ( int( (2147483647-ans)//10**t ) < coeff[i] ) :    
                return 0
        
            ans+=coeff[i]*10**t
            t+=1

        if negative :
            ans*=-1

        return ans

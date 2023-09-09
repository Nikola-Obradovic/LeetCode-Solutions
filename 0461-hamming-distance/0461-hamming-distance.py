class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s1=format(x, '032b')
        s2=format(y, '032b')
        cnt=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                cnt+=1
        return cnt
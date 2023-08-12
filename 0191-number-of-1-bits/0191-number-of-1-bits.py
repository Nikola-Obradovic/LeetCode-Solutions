class Solution:
    def hammingWeight(self, n: int) -> int:
        s = format(n, '032b')
        cnt=0
        for x in range(len(s)):
            if s[x]=="1":
                cnt+=1
        return cnt

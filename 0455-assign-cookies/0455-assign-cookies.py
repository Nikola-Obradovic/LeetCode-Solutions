class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        lens=len(s)
        cnt=0
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j]>=g[i]:
                    cnt+=1
                    s.pop(j)
                    break
        if cnt>lens:
            cnt=lens
        return cnt
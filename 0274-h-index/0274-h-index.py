class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        
        citations.sort()
        n=len(citations)
        h=n
        x=0
        while True:
            if x<n and citations[x]<h and n-x-1<h:
                h-=1
            else:
                return h
            x+=1
                




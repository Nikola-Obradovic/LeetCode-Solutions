class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        l=[]
        cnt=0
        x=len(gifts)-1
        total=0
        while cnt<k:
            gifts.sort()
            gifts[x]=int(sqrt(gifts[x]))
            
          
            
            cnt+=1

        for i in gifts:
            total+=i
        return total

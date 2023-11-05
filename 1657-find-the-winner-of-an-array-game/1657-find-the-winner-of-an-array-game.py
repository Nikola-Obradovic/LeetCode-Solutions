class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cnt=0
        winner=0
        
        while cnt!=k:

            if arr[0]>arr[1]:
                cnt+=1
                temp=arr.pop(1)
                arr.append(temp)
                winner=arr[0]
            else:
                winner=arr[1]
                cnt=1
                temp=arr.pop(0)
                arr.append(temp)
            
            if cnt>len(arr):
                break
        
        return winner
        
        
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cntA=0
        cntB=0

        for i in range(1,len(colors)-1):
            if colors[i]=="A" and colors[i-1]=="A" and colors[i+1]=="A":
                cntA+=1
            if colors[i]=="B" and colors[i-1]=="B" and colors[i+1]=="B":
                cntB+=1

        if cntA>cntB:
            return True
        return False
        
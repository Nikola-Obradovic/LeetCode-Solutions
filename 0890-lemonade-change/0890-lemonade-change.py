class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        twenty=0

        for i in bills:
            if i==5:
                five+=1
            elif i==10:
                five-=1
                if five<0:
                    return False
                ten+=1
            else:
                twenty+=1
                if ten>0:
                    ten-=1
                    five-=1
                else:
                    five-=3
                
                if five<0:
                    return False
                
        
        return True
        
class Solution:
    def addDigits(self, num: int) -> int:
        if num>0 and num<10:
            return num
        
        summ=0
        while num>9:
            summ=0
            while num>0:
                summ+=num%10
                num=num//10
            num=summ
            
        return summ

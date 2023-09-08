class SmallestInfiniteSet:

    def __init__(self):

        self.obj = [i for i in range(1, 1001)]
       

    def popSmallest(self) -> int:
        return self.obj.pop(0)
        

    def addBack(self, num: int) -> None:
        i=0
        while True:
            if num in self.obj:
                break
            if not num in self.obj and self.obj[i]>num:
                self.obj.insert(i,num)
                break
            else:
                i+=1
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
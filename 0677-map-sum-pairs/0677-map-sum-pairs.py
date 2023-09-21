class MapSum:

    def __init__(self):
        self.obj={}
    
        

    def insert(self, key: str, val: int) -> None:
        self.obj[key]=val


    def sum(self, prefix: str) -> int:
        total=0
        for key,value in self.obj.items():
            if prefix in key:
                found=True
                for j in range(len(prefix)):
                    if prefix[j]!=key[j]:
                        found=False
                        break
                if found:
                    total+=value

        return total        



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
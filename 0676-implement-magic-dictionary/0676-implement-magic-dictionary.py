class MagicDictionary:

    def __init__(self):
        self.obj=[]
        

    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            if not i in self.obj:
                self.obj.append(i)
        

    def search(self, searchWord: str) -> bool:
        
        
        for i in range(len(self.obj)):
            cnt=0
            if len(self.obj[i])==len(searchWord):
                
                for j in range(len(self.obj[i])):
                    if self.obj[i][j]!=searchWord[j]:
                        cnt+=1

                if cnt==1:
                    return True
        return False

            


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
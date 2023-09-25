class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l=[]
        index=[]
        least=1000000
        for i in range(len(list1)):
            if list1[i] in list2:
                if i+ list2.index(list1[i])<=least:
                    least=i+ list2.index(list1[i])
                    index.append(i)
                    l.append(least)
        res=[]
        minnum=min(l)
        

        for i in range(len(l)):
            if l[i]==minnum:
                res.append(list1[index[i]])


        return res
        
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start=[]
        end=[]

        for i in range(len(flowers)):
            start.append(flowers[i][0])
            end.append(flowers[i][1])
        
        start.sort()
        end.sort()

        return [bisect_right(start, t) - bisect_left(end, t) for t in people]

        

        
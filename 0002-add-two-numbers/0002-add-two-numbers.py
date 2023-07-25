# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



def Check(num):
    cnt=0
    while num != 0 and num%10==0:
        cnt=cnt+1
        num=num//10
    return cnt



def addToList(nextNode, new_value):
    new_node = ListNode(new_value)
    new_node.next = nextNode
    return new_node

def Reverse(num):
    newnum = 0
    while num > 0:
        newnum = newnum * 10 + num % 10
        num = num // 10
    return newnum

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = 0
        b = 0
        ca=0
        cb=0
        cnta=0
        cntb=0
        while l1 is not None:
            a = a * 10 + l1.val
            if l1.val!=0:
                ca+=1
            
            if l1.val==0 and ca==0:
                cnta+=1


            l1 = l1.next

        while l2 is not None:
            b = b * 10 + l2.val
            if l2.val!=0:
                cb+=1
            
            if l2.val==0 and cb==0:
                cntb+=1
            
            l2 = l2.next


        a1 = Reverse(a)
        b1 = Reverse(b)
        while cnta>0:
            a1*=10
            cnta-=1
        while cntb>0:
            b1*=10
            cntb-=1    



        tempres = a1 + b1
        cnt=Check(tempres)
        res=Reverse(tempres)
        

        l3 = ListNode(res % 10)
        res = res // 10

        while res != 0:
            l3 = addToList(l3, res % 10)
            res = res // 10

        while cnt>0:
            l3 = addToList(l3, 0)
            cnt=cnt-1    

        return l3



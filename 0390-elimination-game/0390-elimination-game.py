class Solution:
    def lastRemaining(self, n: int) -> int:
        left=True
        r=n
        step=1
        head=1

        while r>1:
            if left or r%2==1:
                head+=step
            step=step*2
            r//=2
            left= not left
        return head

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def Search(self, root, d):
        
        if root==None:
            return
        if not root.val in d:
            d[root.val]=1
        else:
            d[root.val]+=1
        
        self.Search(root.left, d)
        self.Search(root.right, d)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        
        self.Search(root, d)

        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        l=[]
        temp=[]
        
        for key,value in d.items():
            temp.append(value)
            if value == temp[0]:
                l.append(key)
            elif value < temp[0]:
                break
        
        return l



        
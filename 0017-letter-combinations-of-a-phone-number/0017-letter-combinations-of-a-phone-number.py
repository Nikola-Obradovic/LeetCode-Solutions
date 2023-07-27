from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        dictionary = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
        l=[]
        for x in digits:
            l.append(dictionary[x])
        combinations = [''.join(chars) for chars in product(*l)]


        return combinations

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l=list(moves)
        if l.count("D")!=l.count("U"):
            return False
        if l.count("L")!=l.count("R"):
            return False
        return True
        
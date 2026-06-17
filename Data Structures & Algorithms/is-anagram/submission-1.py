class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ConvertS, ConvertT = {}, {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            ConvertS[s[i]] = 1 + ConvertS.get(s[i], 0)
            ConvertT[t[i]] = 1 + ConvertT.get(t[i], 0)
        for c in ConvertS:
            if ConvertS[c] != ConvertT.get(c,0):
                return False
        return True 

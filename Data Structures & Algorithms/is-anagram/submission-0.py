class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        CounterS, CounterT = {}, {}

        for i in range(len(s)):
            CounterS[s[i]] = 1 + CounterS.get(s[i], 0)
            CounterT[t[i]] = 1 + CounterT.get(t[i], 0)
        for c in CounterS:
            if CounterS[c] != CounterT.get(c, 0):
                return False
        return True
        
    
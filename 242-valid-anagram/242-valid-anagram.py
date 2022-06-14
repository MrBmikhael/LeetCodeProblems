class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashSetA = dict()
        hashSetB = dict()
        
        for i in s:
            hashSetA[i] = hashSetA.get(i, 0) + 1
                
        for i in t:
            hashSetB[i] = hashSetB.get(i, 0) + 1
        
        if len(hashSetA) != len(hashSetB):
            return False
        
        for i in hashSetA:
            if i not in hashSetB or hashSetA[i] != hashSetB[i]:
                return False
        
        return True
        
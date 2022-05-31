class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        goal = 2**k
        foundHashes = set()
        
        for i in range(0, len(s)-(k-1)):
            substr = s[i:i+k]
            foundHashes.add(substr)

        return len(foundHashes) == goal
        
        
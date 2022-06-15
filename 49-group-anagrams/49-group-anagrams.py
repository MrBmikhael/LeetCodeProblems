class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        
        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l) - ord('a')] += 1
            countStr = str(count)
            if countStr in output:
                output[countStr].append(s)
            else:
                output[countStr] = [s]
        return output.values()
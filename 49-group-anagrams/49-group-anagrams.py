class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        
        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l) - ord('a')] += 1
            if str(count) in output:
                output[str(count)].append(s)
            else:
                output[str(count)] = [s]
        return output.values()
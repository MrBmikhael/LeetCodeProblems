class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        chStack = []
        
        for i in s:
            if len(chStack) > 0 and chStack[-1][0] == i:
                chStack[-1][1] += 1
            else:
                chStack.append([i, 1])

            if chStack[-1][1] == k:
                chStack.pop()
        
        output = ""
        for i in chStack:
            output += (i[0] * i[1])
            
        return output
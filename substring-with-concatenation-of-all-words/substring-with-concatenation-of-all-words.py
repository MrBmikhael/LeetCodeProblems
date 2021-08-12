class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordLen = len(words[0])
        output = list()
        currentWordList = words[:]
        rangeLimit = len(s)-(wordLen*(len(words)-1))

        for i in range(0, rangeLimit):
            j = i
            while len(currentWordList) != 0:
                word = s[j:j+wordLen]
                if word in currentWordList:
                    currentWordList.remove(word)
                    j += wordLen
                else:
                    break
            if len(currentWordList) == 0:
                output.append(i)
            currentWordList = words[:]
            
        return output
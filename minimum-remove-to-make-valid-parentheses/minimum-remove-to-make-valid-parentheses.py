class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = list()
        outputStr = list(s)

        for i in range(len(outputStr)):
            if outputStr[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    outputStr[i] = ''
            elif outputStr[i] == '(':
                stack.append(i)

        while stack:
            index = stack.pop()
            outputStr[index] = ''

        return ''.join(outputStr)
    
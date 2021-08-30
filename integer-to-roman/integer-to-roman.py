class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        output = []
        
        while num >= 1000:
            output.append('M')
            num -= 1000
            
        if num >= 900:
            output.append('CM')
            num -= 900
            
        if num >= 500:
            output.append('D')
            num -= 500
            
        if num >= 400:
            output.append('CD')
            num -= 400
            
        while num >= 100:
            output.append('C')
            num -= 100
            
        if num >= 90:
            output.append('XC')
            num -= 90
        
        if num >= 50:
            output.append('L')
            num -= 50
        
        if num >= 40:
            output.append('XL')
            num -= 40
            
        while num >= 10:
            output.append('X')
            num -= 10
            
        if num >= 9:
            output.append('IX')
            num -= 9
            
        if num >= 5:
            output.append('V')
            num -= 5
            
        if num >= 4:
            output.append('IV')
            num -= 4
            
        while num > 0:
            output.append('I')
            num -= 1
            
        return ''.join(output)
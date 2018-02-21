#8

def atoi(str):
    cstr = str.strip()
    mul = 1
    i = 0
    while i < len(cstr):
        if cstr[i] == '-':
            mul*=-1
            i+=1
        elif cstr[i] == '+':
            i+=1
        else:
            break
    if i == len(cstr):
        return 0
    else:
        return mul*int(cstr[i:])

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        return atoi(str)
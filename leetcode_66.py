#66 ac

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        tmp =0
        rst = []
        i = 0
        while i < len(digits):
            if i == 0:
                tmp = digits[i] + 1 + tmp
            else:
                tmp = digits[i] + tmp

            rst.append(tmp%10)
            tmp = tmp/10
            i+=1
        if tmp > 0:
            rst.append(tmp)
        rst.reverse()
        return rst
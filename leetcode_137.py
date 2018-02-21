#137 ac

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in nums:
            if h.get(i,None) is None:
                h[i] = 1
            else:
                h[i] = h[i]+1
        for k,v in h.items():
            if v == 1:
                return k
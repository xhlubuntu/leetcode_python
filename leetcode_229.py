
#ac
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freqdict = {}
        for i in nums:
            if freqdict.has_key(i):
                freqdict[i] +=1
            else:
                freqdict[i]=1
        m = int(len(nums)/3)
        rst = []
        for k,v in freqdict.items():
            if v>m:
                rst.append(k)
        return rst
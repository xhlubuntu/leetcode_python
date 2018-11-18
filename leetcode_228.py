

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rst = []
        i,j=0,0
        n = len(nums)
        if n ==0:
            return rst
        if n == 1:
            rst.append(str(nums[0]))
            return rst
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[j-1] + 1:
                j+=1
            if j-1==i:
                rst.append(str(nums[i]))
            if j-1<>i:
                rst.append(str(nums[i])+'->' +str(nums[j-1]))
            i = j
        return rst
        

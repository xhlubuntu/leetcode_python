
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for idx,item in enumerate(nums):
            if d.has_key(item):
                d[item].append(idx)
            else:
                d[item] = [idx]
        m = 1000000
        for ki in d.keys():
            if len(d[ki]) > 1:
                for i in range(len(d[ki])-1):
                    m = min(m , d[ki][i+1] - d[ki][i])
        return True if m <= k else False

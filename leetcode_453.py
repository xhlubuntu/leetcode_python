class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minnum = min(nums)
        return sum( map(lambda x:x-minnum , nums) )
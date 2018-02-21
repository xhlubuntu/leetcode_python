#31 wa

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 1:
            return
        x = nums[length-1]
        j = length-2
        while j >=0 :
            if nums[j] < x:
                break
            else:
                j-=1
        if j == -1:
            nums.reverse()
        else:
            k = length-1
            while k>=j+1:
                nums[k],nums[k-1] = nums[k-1],nums[k]
                k-=1






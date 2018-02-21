#75 ac

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0:
            return
        cnt0,cnt1,cnt2 = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt0+=1
            if nums[i] == 1:
                cnt1+=1
            if nums[i] == 2:
                cnt2+=1
        i = 0
        while i < length:
            if i< cnt0:
                nums[i]=0
                i+=1
            elif i< cnt0+cnt1:
                nums[i]=1
                i+=1
            else:
                nums[i] = 2
                i+=1
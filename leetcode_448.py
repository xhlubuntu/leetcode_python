
#ac
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = [0]*(len(nums)+1)
        rst = []
        for i in nums:
            cnt[i] += 1
        #print cnt
        for i in range(1,len(cnt)):
            if cnt[i] == 0:
                rst.append(i)
        return rst

nums = [4,3,2,7,8,2,3,1]
sol = Solution()
sol.findDisappearedNumbers(nums)
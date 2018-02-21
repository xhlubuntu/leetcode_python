
#26 ac

def swap(s,i,j):
    t = s[i]
    s[i] = s[j]
    s[j] = t

class Solution(object):
    def removeDuplicates(self,nums):
        if(len(nums)<=0):
            return 0
        cnt = 1
        j=1
        for i in range(1 , len(nums) ):
            if(nums[i]!=nums[i-1]):
                cnt+=1
                nums[j] = nums[i]
                j+=1
        return cnt

sol = Solution()
print sol.removeDuplicates([1,1,2,2])

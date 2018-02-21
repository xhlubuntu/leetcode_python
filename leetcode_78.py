
#78 ac
def subSetDfs(s,i,tmparr,output):
    if i < len(s):
        output.append( tmparr + [s[i]] )
    for j in range(i+1,len(s)):
        subSetDfs(s,j,tmparr + [s[i]],output)

class Solution(object):
    def subsets(self,nums):
        output = []
        output.append([])
        for i in range(0,len(nums)):
            subSetDfs(nums,i,[],output)
        return output

sol = Solution()
print sol.subSet([1,2,3])

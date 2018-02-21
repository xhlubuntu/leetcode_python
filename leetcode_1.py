#1 ac
class Solution(object):
    def twoSumx(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedNum = sorted(nums)
        retList = []
        i = 0
        while i < len(nums):
            nextNum = target - nums[i]
            if nextNum in sortedNum[i+1:]:
                retList.append(i)
                retList.append(sortedNum.index(nextNum))
            else:
                i+=1
        return retList
    def twoSumy(self,nums,target):
        sortedNums = sorted(nums)
        i = 0
        j = len(nums)-1
        x,y = 0,0
        while i < j:
            if(target == sortedNums[i] + sortedNums[j]):
                x = sortedNums[i]
                y = sortedNums[j]
            elif target > sortedNums[i] + sortedNums[j]:
                i+=1
            else:
                j-=1
        return [nums.index(x) , nums.index(y)]
    def twoSum(self,nums,target):
        valIdxMap = {}
        for idx in range(0,len(nums)):
            #valIdxMap[nums[idx]] = idx
            if valIdxMap.get( nums[idx],None ) is None:
                valIdxMap[ nums[idx] ] = [idx]
            else:
                valIdxMap[nums[idx]].append(idx)

        for val in valIdxMap.keys():
            if valIdxMap.get(target - val,None) is not None:
                if len(valIdxMap[val]) > 1:
                    return valIdxMap[val]
                else:
                    return [ valIdxMap[val][0] , valIdxMap[target - val][0] ]
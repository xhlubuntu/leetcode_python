#15

def threesum(nums):
    negHash = {}
    posHash = {}
    zeroCnt = 0
    retList = []
    for idx,val in enumerate(nums):
        if val < 0:
            negHash[val] = idx
        elif val > 0:
            posHash[val] = idx
        else: # val == 0
            zeroCnt += 1
    for i in range(0,zeroCnt+1):
        if i == 0:
            for posval in posHash.keys():
                for tmpneg in negHash.keys():
                    if negHash.get(  (posval+tmpneg)*-1 , None ) is not None:
                        retList.append( [tmpneg , (posval+tmpneg)*-1 , posval  ] )
            for negval in negHash.keys():
                for tmppos in posHash.keys():
                    if posHash.get( (negval+tmppos)*-1 , None ) is not None:
                        retList.append( [ negval , tmppos , (negval+tmppos)*-1 ])
        if i == 1:
            for posval in posHash.keys():
                if negHash.get(posval*-1,None) is not None:
                    retList.append([posval*-1 , 0 , posval])
        if i == 2:
            continue
        if i == 3:
            retList.append([0,0,0])
    return retList

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return threesum(nums)

import pprint
nums = [-1, 0, 1, 2, -1, -4]
pprint.pprint(threesum(nums))
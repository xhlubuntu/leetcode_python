
#tle

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totaldistance = 0
        lenn = len(nums)
        if(lenn==0):
            return 0
        bins = [bin(t)[2:] for t in nums]
        m = max([len(t) for t in bins])
        fixedbins = ['0'*(m-len(t))+t for t in bins]


        for i in range(0,lenn-1):
            j=i+1
            while(j<lenn):
                totaldistance += self.hdistance(fixedbins[i] , fixedbins[j])
                j+=1
        return totaldistance

    def hdistance(self,a,b):
        return sum( [1 if e[0]!=e[1] else 0 for e in zip(a,b)] )

    def hammingDistance(self,a,b):
        bina ,binb = bin(a)[2:] , bin(b)[2:]
        la , lb = len(bina) , len(binb)
        lm = max(la,lb)
        fixedbina , fixedbinb = '0'*(lm - la) + bina , '0'*(lm - lb) + binb
        return sum( [1 if e[0]!=e[1] else 0 for e in zip(fixedbina,fixedbinb)] )

ns = [4,14,2]
sol = Solution()
sol.totalHammingDistance(ns)
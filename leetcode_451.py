#ac

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freqdict = {}
        for word in s:
            if freqdict.has_key(word):
                freqdict[word] += 1
            else:
                freqdict[word] = 1
        middict = sorted( zip( freqdict.values() , freqdict.keys() ) , key = lambda x:x[0] , reverse=True)
        #print middict
        return ''.join( map(lambda x:x[0]*x[1] , middict) )

sol = Solution()
s = 'tree'
sol.frequencySort(s)
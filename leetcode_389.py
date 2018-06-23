
#ac

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freqdict = {}
        for word in t:
            if freqdict.has_key(word):
                freqdict[word]+=1
            else:
                freqdict[word]=1
        for word in s:
            freqdict[word]-=1
        for k,v in freqdict.items():
            if v == 1:
                return k
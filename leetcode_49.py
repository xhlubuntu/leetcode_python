
#49 ac
class Solution(object):
    def groupAnagrams(self,strs):
        xmap = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if(xmap.get(sortedWord) is None):
                xmap[sortedWord] = [word]
            else:
                xmap[sortedWord].append(word)
        return xmap.values()
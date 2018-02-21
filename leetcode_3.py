#3
# time limited exceed

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxSubSize = 0
        tmpHash = {}
        i = 0
        while i < len(s):
            tmpHash.clear()
            tmpHash[s[i]] = i
            j = i+1
            while j< len(s) and not tmpHash.has_key(s[j]):
                tmpHash[s[j]] = j
                j+=1
            maxSubSize = max(maxSubSize , len(tmpHash.keys()))
            if j< len(s):
                i = tmpHash[s[j]]+1
            else:
                i+=1
        return maxSubSize

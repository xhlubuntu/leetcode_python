
#ac
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        rst = []
        i = 0
        if len(chars) == 0 :
             return []
        while i < len(chars):
            j = i + 1
            while(j<len(chars) and chars[j] == chars[i]):
                j+=1
            if(j-i>=2):
                rst.append(chars[i])
                for t in str(j-i):
                    rst.append(t)
            else:
                rst.append(chars[i])
            i = j
        for v in range(len(rst)):
            chars[v] = rst[v]
        return len(rst)

chars = ["a","a","b","b","c","c","c"]
sol = Solution()
sol.compress(chars)

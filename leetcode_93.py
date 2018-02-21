#93 ac

def func(ip):
    if ip == '0':
        return True
    if ip[:1] == '0' or ip[:2] == '0':
        return False
    return True

def legalIp(iplst):
    length = len(iplst)
    rst = sum( [ 1 if 0<=int(ip)<=255 and func(ip) else 0 for ip in iplst ]  )
    return True if rst == 4 else False

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        if length<4 or length>12:
            return []
        #i,j,k = 0,0,0
        rstips = []
        for i in range(1,4):
            for j in range(1,4):
                for k in range(1,4):
                    t0 = i
                    t1 = i + j
                    t2 = i + j + k
                    if t2 < length:
                        ip = [ s[:t0],s[t0:t1],s[t1:t2],s[t2:] ]
                        if legalIp(ip):
                            rstips.append( '.'.join( ip ) )
        return list(set(rstips))

sol = Solution()
sol.restoreIpAddresses('0000')
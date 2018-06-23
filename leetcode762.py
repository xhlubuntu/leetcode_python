import math
#ac
N = 32*2
primes = [1]*N
primes[0] = primes[1] = 0
i = 2
while(i<N):
    j = 2*i
    while(j<N):
        primes[j] = 0
        j+=i
    i += 1

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        cnt = 0
        for i in xrange(L,R+1):
            if(primes[sum( map(lambda a: 1 if a=='1' else 0 , bin(i)[2:]))]):
                cnt+=1
        return cnt



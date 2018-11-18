import copy
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        f = [1]*10
        u = [0]*10
        for i in range(N-1):
          u[1]=f[6] + f[8]
          u[2]=f[7] + f[9]
          u[3]=f[4] + f[8]
          u[4]=f[3] + f[9] + f[0]
          u[6]=f[1] + f[7] + f[0]
          u[7]=f[2] + f[6] 
          u[8]=f[1] + f[3]
          u[9]=f[2] + f[4]
          u[0]=f[4] + f[6]
          f = copy.copy(u)
        m = pow(10,9) + 7
        return sum(f) % m

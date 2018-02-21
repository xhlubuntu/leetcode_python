#69 ac

import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.floor( math.sqrt(x) ))

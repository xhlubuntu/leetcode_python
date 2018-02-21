#11

# max { (j-i)*min(xj,xi) } ,  0<= i < j <= n-1

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        mostwater = 0
        for i in range(0,len(height)-1):
            for j in range(i+1,len(height)):
                water = (j-i)*min(height[i],height[j])
                if water > mostwater:
                    mostwater = water
        return mostwater
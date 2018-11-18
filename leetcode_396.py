class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        totalsum = sum(A)
        length = len(A)
        flist = []
        initial_f = 0
        for idx , item in enumerate(A):
            initial_f += idx * item
        flist.append(initial_f)
        for i in range(length-1):
            tmp = length - 1 - i
            initial_f += (totalsum - A[tmp] - (length-1)*A[tmp])
            flist.append(initial_f)
        return max(flist)

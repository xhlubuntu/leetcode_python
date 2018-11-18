class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        if sum(citations) == 0:
            return 0
        if len(citations) == 1:
            if citations[0] ==0:
                return 0
            if citations[0] >= 1:
                return 1
        N = len(citations)
        revcit = sorted(citations,reverse = True)
        for h in range(N-1):
            if revcit[h] >= h+1 and revcit[h+1] <= h+1:
                return h+1
        return N

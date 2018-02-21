#56 ac

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

#def mergeInterval(A,B):
#    assert(A.start <= B.start)
#    if A.end < B.start:
#        return A,B
#    else:#A.end>=B.start
#        #update A.end
#        A.end = B.end#
#        return A


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        length = len(intervals)
        if length == 0:
            return []
        intervals.sort(key=lambda x:x.start)
        rstIntervals = []
        curInterval = intervals[0]
        for i in range(1,length):
            toMergeInt = intervals[i]
            if curInterval.end < toMergeInt.start:
                rstIntervals.append(curInterval)
                curInterval = toMergeInt
            else:
                if curInterval.end < toMergeInt.end:
                    curInterval.end = toMergeInt.end
        rstIntervals.append(curInterval)
        return rstIntervals



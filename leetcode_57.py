#57 ac

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals,newInterval):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        length = len(intervals)
        if length == 0:
            return [newInterval]
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



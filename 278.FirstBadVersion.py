class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start < end:
            mid = start + (end - start) / 2
            if isBadVersion(mid):
                # if mid is bad, any version newer than mid is bad.
                end = mid
            else:
                # if mid is good, any version older than mid + 1 is good 
                start = mid + 1
        return start

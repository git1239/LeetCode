class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(map(lambda (i, c): (ord(c) - ord('A') + 1)*(26**(len(s)-1-i)), enumerate(s)))

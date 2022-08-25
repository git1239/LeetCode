
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ans = -1
        
        needle_length = len(needle)
        haystack_length = len(haystack)
        
        if needle_length == 0:
            return ans
        
        if needle_length > haystack_length:
            return ans
        
        for i in range(haystack_length - needle_length + 1):
            if haystack[i : i+needle_length] == needle:
                ans = i
                break
                
        return ans

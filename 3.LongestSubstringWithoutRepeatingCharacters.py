class Solution(object):
    def lengthOfLongestSubstring(self, s):
 
        substr=''
        longest=0
        
        for i in range(len(s)):
            if s[i] not in substr:
                substr+=s[i]
                if len(substr) > longest:
                    longest = len(substr)
            else:
                substr=substr[substr.find(s[i])+1:]+s[i]
                
        return longest

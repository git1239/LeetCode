class Solution:
    def majorityElement(self, nums):
        from collections import Counter
        return Counter(nums).most_common()[0][0]

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """   
        return [num for num in set(nums) if nums.count(num) > len(nums)/3]

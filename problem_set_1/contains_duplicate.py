class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        i = 0
        flag = 0
        for i in range(len(nums)):
            j = i+1
            if j < len(nums):
                if nums[i] == nums[j]:
                    flag = 1
                    break
        if flag == 1:
            return True
        else:
            return False
        
        
        
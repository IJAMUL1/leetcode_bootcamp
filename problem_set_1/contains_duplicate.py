class Solution(object):
    def containsDuplicate(self, nums):
        unique = set()
        for i in (nums):
            unique.add(i)
        
        if len(unique) == len(nums):
            return False
        else:
            return True

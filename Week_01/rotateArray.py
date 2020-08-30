class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums = self.reverse(0,len(nums) - 1, nums)
        nums = self.reverse(0, k - 1, nums)
        nums = self.reverse(k, len(nums) - 1, nums)
        return nums

    def reverse(self, s, e, nums):
        while(s < e):
            nums[s],nums[e] = nums[e],nums[s]
            s += 1
            e -= 1
        return nums
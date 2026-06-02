class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left = 0
        while left + 1 < len(nums):
            right = left + 1
            if nums[left] == nums[right]:
                return True
            left += 1
        return False
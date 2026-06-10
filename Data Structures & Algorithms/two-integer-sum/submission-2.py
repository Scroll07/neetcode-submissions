class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for l in range(len(nums)):
            n = nums[l]
            need = target - n
            if need in d:
                return [d.get(need), l]
            d[n] = l
        return []                


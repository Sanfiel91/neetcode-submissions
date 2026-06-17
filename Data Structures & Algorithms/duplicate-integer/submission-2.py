class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        list_nums = {}
        for x in nums:
            list_nums[x] = 1 + list_nums.get(x, 0)
        for v in list_nums.values():
            if v > 1:
                return True

        return False
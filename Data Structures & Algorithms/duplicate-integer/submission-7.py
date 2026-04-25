class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_num = set()
        for num in nums:
            if num in unique_num:
                return True
            unique_num.add(num)
        return False
        
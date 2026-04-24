class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # Initialize the res array with all values set to 1

        prefix = 1 # Variable for prefix pass
        for i in range(len(nums)): # First pass left to right (prefix product)
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1 # Variable for postfix pass
        for i in range(len(nums) - 1, -1, -1): # Second pass right to left (postfix product)
            res[i] *= postfix
            postfix *= nums[i]
        return res
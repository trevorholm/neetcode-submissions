class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # Store the value and index of each element

        for i, num in enumerate(nums): # Iterate through the array
            difference = target - num  
            if difference in hashMap: # Check if the complement exists in the hash map
                return [hashMap[difference], i] # Return the indices of the current element and it's complement
            hashMap[num] = i 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # Empty hash set to store seen values
        for num in nums: # Iterate through each num in the array
            if num in seen: # If the number is in the hash set
                return True
            seen.add(num) # Add the num to the hash set
        return False
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() 
        l = 0 # Initialize left pointer
        res = 0

        for r in range(len(s)): # Update the r pointer with the for loop
            while s[r] in charSet: # Check if the rightmost char is in the unique set
                charSet.remove(s[l]) # Remove the leftmost char
                l += 1 # Update the left pointer by one, while the duplicate remains in the set
            charSet.add(s[r]) # Add the leftmost char to the set
            res = max(res, r - l + 1) # Update the result to see if a new max length has been found
        return res # Return res

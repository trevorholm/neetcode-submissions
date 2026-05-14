class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # Hashmap to count occurrences of each char
        res = 0 # Result with the longest length 

        l = 0 # Intialize left pointer
        for r in range(len(s)): # Use a for loop to have the right pointer go through every char in the string
            count[s[r]] = 1 + count.get(s[r], 0) # For the char at position r, increment the count of it by one with the previous count, if there is none it will add 0

            while (r - l + 1) - max(count.values()) > k: # Check if current window is valid, check length of the window and subtract the count of the most frequent char and compare that to k
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1) # Update result to check the longest with result and the size of the window
        return res
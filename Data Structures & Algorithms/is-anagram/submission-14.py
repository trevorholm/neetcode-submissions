class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Space: O(1) Time: O(n + m)
        if len(s) != len(t): # If the length of the strings are not equal, they cannot be anagrams
            return False
        
        count = [0] * 26 # letters a to z
        for i in range(len(s)): # Iterate through both strings
            count[ord(s[i]) - ord('a')] += 1 # Increment the count in s
            count[ord(t[i]) - ord('a')] -= 1 # Decrement the count in t
        
        for val in count:
            if val != 0:
                return False # If the value is not 0, the frequencies differ
        return True

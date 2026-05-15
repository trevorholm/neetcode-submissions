class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): # Check to see if s2 smaller than the substring
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26 # A - Z to convert into integers in an array
        for i in range(len(s1)): # Convert the char into integers
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26): # If the letter matches, increase match count
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # SLIDING WINDOW PORTION
        l = 0 # Initialize left pointer
        for r in range(len(s1), len(s2)): # Intialize right pointer in for loop and have the window be the start of s1
            if matches == 26: return True # If the substring hits 26 matches, then return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
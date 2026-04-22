class Solution:
    def checkValidString(self, s: str) -> bool:
        # Space: O(1) Time: O(n)

        leftMin, leftMax = 0, 0 # leftMin for left paren, leftMax for right paren

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1 # Increment both var
            elif c == ")": 
                leftMin, leftMax = leftMin - 1, leftMax - 1 # Decrement both var
            else: # Wildcard case
                leftMin, leftMax = leftMin - 1, leftMax + 1 # leftMin as ')', leftMax as '('
            
            if leftMax < 0:
                return False # Too many closing parentheses, impossible for paren to be valid
            if leftMin < 0: 
                leftMin = 0 # Reset back to zero
        return leftMin == 0